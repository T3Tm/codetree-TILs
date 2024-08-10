import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[][] arr = new int[102][102];
    static int n,k,u,d;
    public static class Pair{
        int x,y;
        
        public Pair(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    public static void InputPart() throws IOException{
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        u = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        for(int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0;j<n;j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
            
        }
    }

    //최댓값 지정
    static int maxValue = -1;
    static int[] dx = {0,0,1,-1};
    static int[] dy = {1,-1,0,0};

    
    public static void bfs(Pair[] pick){
        Queue<Pair> q= new LinkedList<>();
        boolean[][] visited = new boolean[102][102];
        for(int i=0;i<k;i++){
            q.offer(pick[i]);    
            visited[pick[i].x][pick[i].y] = true;
        }

        int cnt = 0;
        while(!q.isEmpty()){
            Pair cur = q.poll();
            cnt++;
            for(int i=0;i<4;i++){
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if(nx < 0 || nx >= n || ny < 0 || ny >=n)continue;//경계면 체크
                //높이 차이 
                if(Math.abs(arr[cur.x][cur.y] - arr[nx][ny])< u || Math.abs(arr[cur.x][cur.y] - arr[nx][ny]) > d)continue;
                if(visited[nx][ny])continue;
                q.offer(new Pair(nx,ny));
                visited[nx][ny] = true;
            }
        }
        maxValue = Math.max(maxValue, cnt);
    }

    public static void PickingK(int x, int y, int depth, Pair[] pick){
        if(depth == k){// K개 다 뽑음
            //k번 다 움직임
            bfs(pick);//뽑은 좌표들로 하여금 maxValue 찾기
            return;
        }
        
        for(int i=x;i<n;i++){
            for(int j=y;j<n;j++){
                pick[depth] = new Pair(i,j);//현재 지점 넣기
                PickingK(i,j+1,depth+1,pick);//현재 지점 넣었다고 생각하고 움직이기
                pick[depth] = new Pair(-1,-1);//현재 지점 빼기
            }
            y = 0;
        }
    }
    // k개의 조합을 뽑는다. 
    public static void process(){
        Pair[] pick = new Pair[4];//k는 최대 3
        //1. k개 조합 뽑기
        PickingK(0,0,0,pick);
        //최댓값 출력
        System.out.println(maxValue);
    }

    public static void main(String[] args) throws IOException{
        // 여기에 코드를 작성해주세요.
        InputPart();//입력 받기
        process();//실행
    }
}