from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

grade_db = [
  {
    "_id": "24a24058-7cd3-4b9b-A4db-1391fe6ab1b9",
    "index": "1",
    "teacher": "궉현성",
    "phone": "010-7629-8061",
    "grade": "3",
    "num": "3",
    "contents": "쓸쓸하랴 얼마나 하늘에는 부인한다 근로자는 아이들의 형사상 관한. 교육재정 아름다운"
  },
  {
    "_id": "1e7cbad4-a848-404d-B325-2565d2596ad5",
    "index": "2",
    "teacher": "허은서",
    "phone": "010-2654-0711",
    "grade": "2",
    "num": "14",
    "contents": "원장의 약동하다 정치에 피다 물공급·포로·군용물에 조력을 듯합니다 별이. 공개회의에서 군영과"
  },
  {
    "_id": "23149824-1616-440d-C437-8248b6e8746a",
    "teacher": "3",
    "name": "조근우",
    "phone": "010-9726-8627",
    "grade": "1",
    "num": "1",
    "contents": "위하여서옥 쓸쓸하랴 뜨고 주며 선거권을 권익의 부서한다 권리. 응하기 되려니와"
  },
  {
    "_id": "ce3526b9-ce55-46ea-Cc41-99849084906b",
    "index": "4",
    "teacher": "어혜영",
    "phone": "010-7246-2968",
    "grade": "3",
    "num": "5",
    "contents": "있는 실현에 둔다 아니하며 멀듯이 구하지 토끼 존속하며. 대한민국은 이용·개발과"
  },
  {
    "_id": "123688af-cc3e-4675-A38b-28806e57157d",
    "index": "5",
    "teacher": "궉도겸",
    "phone": "010-8724-1191",
    "grade": "3",
    "num": "2",
    "contents": "붙여 가할 하늘에는 아니한다 트고 의하여 향상을 눈이. 별들을 후"
  }
]

def index(request):
    return render(request, 'main/index.html')

def jejuohyun(request):
    return render(request, 'main/jejuohyun.html')

def grade(request):
    return render(request, 'main/grade.html')

def my_page(request):
    return render(request, 'main/my_page.html')
