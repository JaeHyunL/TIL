from collections import defaultdict, namedtuple
# BETTER WAY 37 내장타입을 여러 단계로 내포시키기보다는 클래스를 합성하라.
# 파이썬 내장 딕셔너리 타입을 사용하면 객체의 생명주기 동안 동적인 내부 상태를 잘
# 유지할 수 있다. 여기서 동적이라는 말은 어떤 값이 들어올지 미리 알수없는 식별자들을
# 유지해야한다는 뜻이다. 예를들어 학생들의 점수를 기록해야 하는데 학생의 이름은 미리 알수 없는 상황이라고 하자.
# 이럴 때는 학생별로 각 항생의 이름을 사용해 미리 정의된 애트리뷰트를 사용하는 대신
# 딕셔너리에 이름을 저장하는 클래스를 정의할 수 있다.


class SimpleGradeBook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name: str):
        self._grades[name] = []

    def report_grade(self, name: str, score: int):
        self._grades[name].append(score)

    def average_grade(self, name: str):
        grades = self._grades[name]
        return sum(grades) / len(grades)


book = SimpleGradeBook()
book.add_student('아이작 뉴턴')
book.report_grade('아이작 뉴턴', 90)
book.report_grade('아이작 뉴턴', 95)
book.report_grade('아이작 뉴턴', 85)

print(book.average_grade('아이작 뉴턴'))
# 딕셔너리와 관련 내장 타입은 사용하기 너무 쉬으므로 과하게 확장하면서
# 깨지기 쉬운 코드를 작성할 위험성이 있다. 예를 들어 SimpleGradeBook 클래스를 확장해서
# 전체 성적이 아니라 과목별 성적을 리스트로 저장하고 싶다고 하자. _grades 딕셔너리를 변경해서
# 학생 이름(키)이 다른 딕셔너리(값)로 매핑하게 하고, 이 딕셔너리가 다시 과목(키)을 성적의
# 리스트(값)에 매핑하게 함으로써 과목별 성적을 구현할 수 있다. 다음 코드는 내부 딕셔너리로
# defaultdict의 인스턴스를 사용해서 과목이 없는 경우를 처리한다(BETTER way 17: '내부 상태에서 원소가 없는 경우를 처리할
# 때 는 setdefault보다 defaultdict를 사용하라' 에서 배경 지식을 얻을 수 있다.


class BySubjectGradeBook:
    def __init__(self):
        self._grades = {}  # 외부 딕셔너리

    def add_student(self, name: str):
        self._grades[name] = defaultdict(list)  # 내부 딕셔너리 에러 처리 예방

    def report_grade(self, name: str, subject: str, grade: int):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(grade)

    def average_grade(self, name: str):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


book = BySubjectGradeBook()
book.add_student('알버튼 아인슈타인')
book.report_grade('알버튼 아인슈타인', '수학', 75)
book.report_grade('알버튼 아인슈타인', '수학', 65)
book.report_grade('알버튼 아인슈타인', '체육', 90)
book.report_grade('알버튼 아인슈타인', '체육', 95)
print(book.average_grade('알버튼 아인슈타인'))

# 이 코드는 아주 평이하다. 다단계 딕셔너리를 처리 해야 하므로 report_grade와 average_grade 메서드가
# 많이 복잡해지지만, 아직은 충분히 복잡도를 관리할 수 있을것 같다.

# 이제 요구 사항이 또 봐뀐다. 각 점수의 가중치를 함께 저장해서 중간고사와 기말고사가
# 다른 쪽지 시험보다 성적에 더 큰 영향을 미치게 하고싶다. 이런 기능을 구현하는 한 가지
# 방법은 가장 안쪽에 있는 딕셔너리가 과목(키)을 성적의 리스트(값)로 매핑하던 것을 (성적, 가중치) 튜플의 리스트로
# 매핑하도록 변경하는 것이다.


class WeightedGradeBook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name: str):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name: str, subject: str, score: int, weight: float):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight))

    def average_grade(self, name: str):
        by_subject = self._grades[name]

        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0

            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight

            score_sum += subject_avg / total_weight
            score_count += 1

            return score_sum / score_count

# report_grade에는 아주 단순한 병겨만 일어났다 (성적 리스트가 튜플 인스턴스를 저장하게
# 했을 뿐이다). 하지만 변경된 average_grade 메서드는 루프 안에 루프가 쓰이면서 읽기 어려워졌따.


book = WeightedGradeBook()
book.add_student('알버튼 아인슈타인')
book.report_grade('알버튼 아인슈타인', '수학', 75, 0.05)
book.report_grade('알버튼 아인슈타인', '수학', 65, 0.15)
book.report_grade('알버튼 아인슈타인', '수학', 70, 0.80)
book.report_grade('알버튼 아인슈타인', '체육', 100, 0.40)
book.report_grade('알버튼 아인슈타인', '체육', 85, 0.60)
print(book.average_grade('알버튼 아인슈타인'))


# 딕셔너리안에 딕셔너리를 떄려 넣은 순간 유지복수 악몽의 시작이며 다른사람이 읽기 힘들 수 가 있다.
# 코드에서 값을 관리하는 부분이 점점 복잡해지고 있음을 깨닫는 즉시 해당 기능을
# 클래스로 분리해야한다. 이를 통해 여러분의 데이터를 더 잘 캡슐화 해주는 인터페이스와
# 구체적인 구현 사이에 잘 정의돈 추상화 계층을 만들 수 도 있따.

grades = []
grades.append((95, 0.45))
grades.append((85, 0.55))
total = sum(score * weight for score, weight in grades)
total_weight= sum(weight for _, weight in grades)
average_grade = total / total_weight

# total_weight 를 계산할 때는 _(파이썬에서 사용하지 않는 변수 이름을 표시할 때 관례적으로 사용하는 변수이름)
# 사용해 각 점수 튜플의 첫 원소를 무시하였다.

# 이 코드의 ㅁ ㅜㄴ제점은 튜플에 저장된 내부 원소에 위치를 사용해 접근한다는 것이다. 예를 들어 선생님이 메모를 추가
# 해야해서 튜플이 늘어 났다고하자 이런 경우 특정 인덱스를 무시하기 위해 비용이 더 많이 든다.

grades = []
grades.append((95, 0.45, '참 잘했어요'))
grades.append((85, 0.55, '조금 더 열심히'))
... # 중략

# 이런식으로 튜플을 좀 더 확장하는 패턴은 딕셔너리를 여러 단계로 내포시키는
# 경우와 유사하다. 원소가 세 개 이상인 튜플을 사용한다면 다른 접근 방법을 생각해봐야 한다.
# collection 내장 모듈에 있는 namedtuple 타입이 이런 경우에 딱 들어 맞는다.
# namedtuple을 사용하면 불변 데이터 클래스를 쉽게 정의할 수 있다.

Grade = namedtuple("grade", ('score', 'weight'))
# 이 클래스의 인스턴스를 만들 떄는 위치 기반 인자를 사용해도 되고 키워드 인자를 사용해도 된다.
# 필드에 접근할 떄는 애트리뷰트 이름을 쓸 수 있다.
# 이름이 붙은 애트리뷰트를 사용할 수 있으므로 유가 사항이 바뀌는 경우에
# namedtuple을 클래스로 변경하기도 쉽다. 예를 들어 가변성을 지원해야 하거나
# 간단한 데이터 컨테이너 이상의 동작이 필요한 경우 namedtuple을 쉽게 클래스로 바꿀 수 있다.

# note namedtuple의 한계
# namedtuple이 유용한 상황이 득보다 실이 많은 경우도 있다는 사실을 잊지 말아야한다.
# namedtuple 클래스에는 디폴트 인자 값을 지정할 수 없다. 따라서 선택적인 프로퍼티가 많은 데이터에 namedtuplem을
# 사용하기가 어렵다. 프로퍼티가 4~5개보다 더 많아지만 dataclasses 내장 모듈을 사용하는 편이 낫다.

# 여전히 namedtuple 인스턴스의 애트리뷰트 값을 숫자 인덱스를 사용해 접근 할 수 있고 이터레이션도 가능하다.
# 특히 외부에 제공하는 API의 경우 이런 특성으로 인해 나중에 namedtuple을 실제 클래스로 변경하기 어려울 수도 있다.
# 여러분이 namedtuple을 사용하는 모든 부분을 제어할 수 있는 상황이 아니라면 명시적으로 새로운 클래스를 정의하는 편이 더 낫다.

# 이제 일련의 점수를 포함하는 단일 과목을 표현하는 클래스를 작성할 수 있다.


class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

# 다음 으로 한 학생이 수강하는 과목들을 표현하는 클래스를 작성할 수 있다.


class Studnet:
    def __init__(self):
        self._subjects = defaultdict(Subject)

    def get_subject(self, name):
        return self._subjects[name]
    
    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

# 마지막으로 모든 학생을 저장하는 컨테이너를 만들 수 있다. 이때 이름을 사용해 동적으로 학생을 저장한다.


class GradeBook:
    def __init__(self):
        self._students = defaultdict(Studnet)

    def get_student(self, name):
        return self._students[name]

# 이렇게 만든 클래스들의 코드 줄 수는  예전 구현한 코드의 두배 이상이다.
# 하지만 새 코드가 더 읽기는 쉽다. 확장성 도 더 좋아졌다.


book = GradeBook()
albert = book.get_student('알버튼 아인슈타인')
math = albert.get_subject('수학')
math.report_grade(75, 0.05)
math.report_grade(65, 0.15)
math.report_grade(70, 0.80)
gym = albert.get_subject('체육')
gym.report_grade(100, 0.40)
gym.report_grade(85, 0.60)
print(albert.average_grade())


'''
    기억해야 할 내용
    딕셔너리, 긴 튜플 다른 내장 타입이 복잡하게 내포된 데이터를 값을 사용하는 딕셔너리를 만들지마라.
    완전한 클래스가 제공하는 유연성이 필요하지 않고 가벼운 불변 데이터 컨테이너가필요하다면 namedtuple을 사용하라.
    내부 상태를 표현하는 딕셔너리가 복잡해지면 이 데이터를 관리하는 코드를 여러 클래스로 나눠서 재작성 하라.
'''
