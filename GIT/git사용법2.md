# GIT이란? (2)

### git revert
- 특정 commit을 없었던 일로 만드는 작업
- `git revert <commit id>`
- 작동원리
    - 재설정
    - 단일 commit을 실행 취소 하는 것
    - 프로젝트 기록에서 commit을 없었던 일로 처리 후 그 결과를 새로운 commit으로 추가함
- 커밋을 삭제하는게 아닌 삭제하고자 하는 커밋이 삭제된 커밋을 만든다.
- 왜 삭제를 안하고 기록으로 새로 만들까?
    - 만약 삭제를 하게 된다면 push를 할 때 문제가 생길 수 있다 왜냐하면 push는 이전과 상황이 같아야 하는데 삭제가 된다면 아예 다른 상황이 되어버리기 때문에

즉, 변경 사항을 안전하게 실행 취소할 수 있도록 도와주는 순방향 실행 취소 작업인 셈이다. commit기록에서 commit을 삭제하거나 분리하는 대신, 지정된 변경사항을 반전시키는 새 commit을 생성하는 것이다.

### git reset
- 특정 commit으로 되돌아 가는 작업
- `git reset [옵션] <commit id>`
- git reset의 작동 원리
   - 되돌리기
   - 시계를 마치 과거로 돌리는 듯한 행위
   - 특정 commit으로 되돌아 갔을 때, 되돌아간 commit 이후의 commit은 모두 삭제!!
- git reset의 옵션 (강도조절)
    - --soft
    <br>삭제된 commit의 기록을 staging area에 남김
    - --mixed
    <br>삭제된 commit의 기록을 working directory에 남김(디폴트값)
    - --hard
    <br>삭제된 commit 기록을 남기지 않음
    - 삭제되는 commit들의 기록을 어떤 영역에 남겨둘 것인지 옵션을 통해서 조정할 수 있음

### git reflog
- HEAD가 이전에 가리켰던 모든 commit을 보여줌
- reset의 --hard 옵션을 통해 지워진 commit도 reflog로 조회하여 복구 가능


### git restore
- Modified 상태의 파일 되돌리기
<br>복구 불가능... 왜? 원래 파일로 덮어쓰는 원리이기 때문에 수정한 내용은 모두 사라진다. Working Directory에서 파일을 수정한 뒤, 파일의 수정 사항을 취소하고, 원래 모습대로 되돌리는 작업

### git rm —cached
- Staging Area에서 Working Directory로 되돌리기
git 저장소에 commit이 없는 경우
### git restore —staged
- Staging Area에서 Working Directory로 되돌리기
 git 저장소에 commit이 존재하는 경우


 ### commit수정하기
 - commit 메세지 수정
 - commit 전체 수정
 - 명령어는 같다 `git commit —-amend`
- 버전관리 측면에서 봤을 때,
”앗, 빠진 파일 넣었음”, “이전 commit에서 오타 살짝 고침” 과 같은 commit은 유효한 버전이라고 보기 어려움
- 즉, 불필요한 commit을 생성하지 않고, 직전 commit을 수정할 수 있기 때문에 git에서 꼭 필요한 기능 중에 하나라고 볼 수 있음

### 느낀점
- 분명 배웠던 내용이였는데 잘 사용하지 않으면서 까먹은 것 같았다..
- 실습을 통해서 다시 한 번 어떻게 사용하는지 알 수 있었다.
- 배운 내용들을 정리해서 계속 보는 습관이 중요하다는 것을 알았다.