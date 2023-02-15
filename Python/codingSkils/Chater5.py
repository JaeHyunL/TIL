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

# BETTER WAY 38 간단한 인터페이스의 경우 클래스 대신 함수를 받아라
# 파이썬 내장 API중 상다수는 함수를 전달해서 ㄷ공작을 원하는 대로 바꿀 수 있게 해준다.
# API가 실행되는 과정에서 여러분이 전달한 함수를 실행하는 경우
# 이런 함수를 hook이라고 부른다. 예를 들어 리스트 타입의 sort메서드는
# 정렬 시 각 인덱스에 대응하는 비교ㄱ 값을 결정하는 선택적인 key 인자를 받을 수 있다.
# 다음 코드는 key 훅으로 len 내장 함수를 전달해서 이름이 들어 있는 리스트를 이름의 길이에 다라 정렬한다.

names = ['소크라테스', '아르키메데스', '플라톤', '아리스토텔레스']
names.sort(key=len)
print(names)

# 훅은 추상 클래스를 통해 정의해야하는 언어도 있지만 파이썬에서는 단수히 인자와 반환값이 
# 잘 정의된 상태가 없는 함수를 훅으로 사용하는 경우가 많다. 
# 함수는 클래스보다 정의하거나 기술하기 더 쉬우므로 훅으로 사용하기에는
# 함수가 이상적이다. 또한 파이썬은 함수를 일급 시민 객체로 취급하기 때문에
# 함수를 훅으로 사용할 수 잇다.
# 함수나 메서드가 일급 시민 객체라는 말은 파이썬 언어레서 사용할 수 있는 다른 일반적인 값과 마찬가지로
# 함수나 메서드를 다른 함수에 넘기거나 변수등으로 참조할 수 있다는 의미이다.

# 예를들어 defaultdict 클래스의 동작을 사용자 정의하고 싶다고 하자


def log_missing():
    print('키 추가됨')
    return 0
# 원본 딕셔너리와 변경할 내용이 주어진 경우, log_missing 함수는 로그를 두번 남길 수 있다.
# (각 로그는 red and orange)에 해당한다.


current = {'초록': 12, '파랑': 3}

increments = [
    ('빨강', 5),
    ('파랑', 17),
    ('주황', 9),
    ('그린이', 1)
]

result = defaultdict(log_missing, current)
print('이전: ', dict(result))
for key, amount in increments:
    result[key] += amount

print('이후: ', dict(result))

# log_missoinsing 과 같은 함수를 사용할 수 있으면 정해진 동작과 부수 효과를 분리할 수 있기 때문에
# API를 더 쉽게 만들 수 있따.
# defaultdict에 전달하는 디폴드 값이 훅이 존재하지 않는 키에 접근한 총횟수를 제공하고 싶다.
# 이런 기능을 만드는 방법중 하나는 상태가 있는 클로저 함수를 사용하는 것이다.
# 다음 코드는 이런 클로저가 있는 도우미 함수를 디폴트 값 훅으로 사용한다.

def increments_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count  # 상태가 있는 함수
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count

result, count = increments_with_report(current, increments)
# assert count == 3
print(result, count)

# 하지만 상태를 다루기 위한 훅으로 클로저를 사용하면 상태가 없는 함수에 비해 읽기 이해하기 어렵다.
# 다른 접근 방법은 여러분이 추적하고 싶은 상태를 저장하는 작은 클래스를 정의하는것이다.


class CountMissing:
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

# 다른 언어에서는 COUNTMISSING이 제공하는 인터페이스를 만족하기 위해 DEFAULTdICT코드를 변경해야 할 수도 있지만
# 파이썬에서는 일급함수 이므로 사용할 객체에 대한 COUNTMISSING.missing
# 메서드를 직접 defaultdict의 디폴트값 훅으로 전달 할 수 있따.
# 어떤 함수 인터페이스를 만족하는 객체인스턴스를 만드는것은 아주 쉽다.


counter = CountMissing()
result = defaultdict(counter.missing, current)  # 메서드 참조
for key, amount in increments:
    result[key] += amount
assert counter.added == 3



# 이 코드를 보면 알 수 있듯이 도우미 클래스로 상태가 있는 클로저와 같은 동작을 제공하는 것이 increments_with_report
# 같은 함수를 사용하는 것 보다 더 깔끔하다 하지만 클래스 자체만 놓고 보면 CountMissing 클래스의 목적이 무엇인지
# 분명히 알기는 어렵다. 누가 CountMissing 클래스의 목적이 무엇인지 분명히 알기는 어렵다
# snrk CountMissing 객체를 만들까? 누가 missing메서드를 호출할까? 이클래스에 나중에 공개메서ㅏ드가 더 추가 될 수도
# 있을까? DefaultDict 와 함께 사용하는 예제를 보기 전까지 이클래스는 수수낄분ㅇ다]]

# 이런 경우를 더 명확히 표현하기 위해서는 파이썬에서는 클래스에 __call__ 특별 메서드를 정의할 수 있따.
# 특별 메서드 __call__을 사용하면 객체를 함수처럼 호출 할 수 있따.
# 그리고 __call__이 정의돈 클래스의 인스턴스에 대해서는 callable 내 장함수를 호출하면
# 다른 함수나 메서드 처럼 True 가 반환된다.
# 이런 방식으로 정의돼서 호출 할 수 있는 객체를 Callable 객체라고 부른다.


class BetterCountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


counter = BetterCountMissing()

assert counter() == 0
assert callable(counter)

counter = BetterCountMissing()
result = defaultdict(counter, current)  # __call__에 의존함
for key, mount in increments:
    result[key] += amount
assert counter.added == 3

# 이 코드가 CountMissing,missing을 사용한 코드 보다 훨 씬 깔끄마핟.
# __call__ 메서드는 API 훅처럼 함수가 인자로 쓰일 수 있는 부분에 이 클래스의
# 인스턴스를 사용할 수 있다는 사실을 나타낸다. 코드를 처음 읽는 사용자 들이
# 이 클래스의 동작을 알아보기 위한 시작점이 __call__ㅇ 이라는 사실을 쉽게 알 수 잇으며
# 이 클래스를 만든 목적이 상태를 저장하는 클로저 역할이라는 사실을 잘 알 수 있다.

# 무엇보다 가장 좋은 점은 defaultdict가 __call__ 내부에서 어떤 일이 벌어지는지에 대해
# 전혀 알 필요가 없다는 사실이다. defaultdict에게 필요한 것은 키가 업슨ㄴ 경우 처리하기 위한
# 디폴트 값 훅 뿐이다. 파이썬은 단순한 함수 인터페이스를 만족시킬 수 잇는 여러가지 방법을 제공하며
# 여러분은 원하는 목적에 가장 적합하는 방식을 선택하면 된다.

"""
    기억해야 할 나용
    파이썬은 여러 컴포넌트 사이에 간단한 인터페이스가 필요할 떄는 클래스를 정의하고 인스턴스 화 하는 대신 간단히 함수를 사용할 수 있다.

    파이썬 함수나 메서드는 일급시민이다. 따라서 함수나 함수 참조식에 사용할 수 있다.

    __call__특별 메서드를 사용하면 클래스의 인스턴스인 객체를 일반 파이썬 함수 처럼 호출 할 수 있다.

    상태를 유지하기 위한 함수가 필요한 경우에는 상태가 있는 클로저를 정의하는 대신__call__메서드가 있는 클래스를 정의할지 고려해보자.
"""

# Better way 39 객체를 제너릭하게 구성하려면 @classmethod를 통한 다형성을 활용하라
# 파이썬에서는 객체뿐만 아니라 클래스도 다형성을 지원한다. 클래스가 다형성을 지원한다는 말은 무슨 뜻일까?
# 왜 클래스가 다형성을 지원하면 좋을까?
# 다형성을 사용하면 계층을 이루는 여러 클래스가 자신에게 맞는 유일한 메서드 버전을 구현할 수 있다.
# 이는 같은 인터페이스를 만족하거나 같은 추상 기반 클래스를 공유하는 많은 클래스가 서로 다른
# 기능을 제공할 수 있다는 뜻이다.(Better way 43: '커스텀 컨테이너 타입은 collections.abc를 상속하라'를 참고)
# 예를 들어 맵리듀스 구현을 하나 작성하고 있는데 입력 데이터를 표현할 수 있는 공통 클래스가 필요하다고 하자.
# 다음 코드는 이럴때 사용하기 위해 정의한 하위클래스에서 다시 정의해야하만 하는 read 메서드가 들어있는 공통 클래스를 보여준다.


class InputData:
    def read(self):
        raise NotImplementedError

# 이 인풋데이터의 구체적인 하위클래스를 만들면서 디스크에서 파일을 읽게 할 수 있다.
class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        with open(self.path) as f:
            return f.read()

# PathInputData와 같이 원하면 얼마든지 InputData의 하위 클래스를 만들 수 있다.
# 각 하위 클래스는 처리할 데이터를 돌려주는 공통 read 인터페이스를 구현해야한다.
# 어떤 InputData의 하위 클래스는 네트워크에서 데이터를 읽을 수 있고, 또 다른 하위클래스는 읽어온 압축
# 데이터를 투명하게 풀어서 제공할 수도 있다. 가능성은 무공무진하다.

# 비슷한 방법으로 이 입력 데이터를 소비하는 공통바법으로 제공하는 맵리듀스 작업자로 쓸 수 있는 추상인터페이스를
# 정의하고 싶다.


class Worker:
    def __init__(self, input_data):
        self.input_data = Input_data
        self.result = None

    def map(self):
        raise NotImplementedError