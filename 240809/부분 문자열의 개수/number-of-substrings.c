#include <stdio.h>
#include <string.h>
/*
    이런 식으로 target의 크기를 2로 지정 후 출력해보면
     str 값이 없는 것으로 나오는데 어떤 문제인지 궁금했습니다.
*/
int main() {
    // 여기에 코드를 작성해주세요.
    char str[1001];
    char target[3];
    int cnt=0;
    
    scanf("%s", str);
    scanf("%s", target);

    
    int len=strlen(str)-1;
    for(int i=0; i<len; i++){
        if(str[i]==target[0] && str[i+1]==target[1]) cnt++;
    }

    printf("%d", cnt);
    
    return 0;
}