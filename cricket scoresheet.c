#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<windows.h>
#include<time.h>
COORD coord={0,0};
typedef struct player
{
    char pnam[25];
    int runbal,ball,strike_rate,runbat,over,wckt;
}player;
typedef struct team
{
    char tnam[40];
    player play[11];
}team;
team teamA,teamB;
int b=0,nb=1;
char mnam[50];

void welcome1();
void welcome2();
void players(team*);
void game(team*,team*);
void greater();
void smaller();
void wgreater();
void wsmaller();
void gotoxy(int x,int y);
void delay(unsigned int mseconds);

int main()
{
    welcome1();
    system("cls");
    welcome2();
    system("cls");
    players(&teamA);
    players(&teamB);
    system("cls");
    printf("\t\t\t%c%cTHE GAME BEGINS HERE!%c%c\n\n\n",178,178,178,178);
    char c,t;
    int i,j,k,a,l,x=6,p[11]={0},q[11]={0},over[50],ball[15],teamrun=0;

    printf("\t\t\t!PRESS 'w' for wide\n\t\t\t!PRESS 'x' for wicket\n\t\t\t!PRESS 'n' for no ball\n");
    printf("\n\t\t\tEnter the runs:\n");
    for(j=1;j<=2;j++)
    {
        x=6;
        int overrun=0;
        printf("\n\t\t\tEnter the bowler number:");
        scanf("%d",k);
    for(i=1;i<=x;i++)
    {
        printf("\n\t\t\tball %d:",i);
//scanf("%c",&c);
c=getche();
fflush(stdin);
        switch(c)
        {
    case '1':
    case '3':
        {
            p[b]+=(c-48);
            overrun+=(c-48);
            teamrun+=(c-48);
            if(b>nb)
                greater();
            else
                smaller();

                break;
        }
    case '2':
    case '4':
    case '6':
    case '0':

        {
            p[b]+=(c-48);
            overrun+=(c-48);
            teamrun+=(c-48);
            break;
        }
    case 'w':


        {
            int v;
            printf("\n\t\t\tEnter the run:");
            scanf("%d",&v);
            teamrun+=(v+1);
            overrun+=(v+1);
            x++;
            if (v==1 || v==3)
            {
                if(b>nb)
                greater();
            else
                smaller();
            }
            break;
        }
    case 'x':
        {
            printf("\n\t\t\t%s is out scoring %d run",teamA.play[b].pnam,p[b]);
            if(b>nb)
                wgreater();
            else
                wsmaller();
            break;
        }
        case 'n':

        {
            int v;
            printf("\t\t\tEnter the run");
            scanf("%d",&v);
            teamrun+=1;

            p[b]+=v;
            overrun+=(v+1);
            teamrun+=v;
            x++;
            if (v==1 || v==3)
            {
                if(b>nb)
                greater();
            else
                smaller();
            }
            break;
        }




    }
    }
    if(b>nb)
                greater();
            else
                smaller();

    }
    //printf("the runs are %d,%d,%d,%d\n",p[0],p[1],p[2],p[3]);
    for(i=0;i<11;i++)
    {
        teamA.play[i].runbat=p[i];
    }
    //printf("teamrun=%d",teamrun);
    for(i=0;i<11;i++)
    {
        teamB.play[i].runbal=q[i];
    }


    //game(&teamA,&teamB);
   // game(&teamB,&teamA);

    return 0;
}
void welcome1()
{
     int i,j;
  gotoxy(35,5);
  printf("%c",218);
  for(i=0;i<35;i++)
  printf("%c",205);

  printf("%c",191);
  for(i=0;i<10;i++){
  gotoxy(35,6+i);
    printf("%c",206);
    gotoxy(71,6+i);
    printf("%c",206);
  }
  gotoxy(35,16);
  printf("%c",192);
for(i=0;i<35;i++)
      printf("%c",205);
    printf("%c",217);
     gotoxy(44,7);
    for(i=0;i<20;i++){
   printf("%c",244);
    }
    delay(1000);
gotoxy(37,9);printf("\t\t!!!WELCOME!!!");
delay(1000);
gotoxy(43,10);printf("@\t\t\t@");
gotoxy(53,10);printf("TO");
delay(1000);
gotoxy(42,12);printf("%c\t\t\t %c",178,178);
gotoxy(44,12);printf("!CRICKET SCORESHEET!");
delay(1000);
gotoxy(25,20);printf("Project by:");
gotoxy(25,22);printf("074BCT506");
gotoxy(25,23);printf("074BCT508");
gotoxy(25,24);printf("074BCT521");
printf("\n\n");
for(i=0;i<30;i++)
{
    printf("\n");
    delay(200);
}
}
void welcome2()
{
    printf("\n\n\t\tEnter the match name:");
    gets(mnam);
    printf("\n\n\t\tEnter batting team name:");
    gets(teamA.tnam);
    printf("\n\t\tEnter balling team name:");
    gets(teamB.tnam);
}
void players(team *a)
{

    int i;
    printf("\n\n\t\t\t%cTEAM SQUAD%c",175,174);
    printf("\n\n\t\t\t%cEnter the names of players of team %s:\n",190,a->tnam);
    for(i=0;i<11;i++)
    {
        printf("\t\t\tplayer %d:",i+1);
        gets(a->play[i].pnam);
    }
}
void greater()
{
    int temp=b;
    b-=(b-nb);
    nb+=(temp-nb);
}
void smaller()
{
    int temp=b;

    b+=(nb-b);
    nb-=(nb-temp);
}
void wgreater()
{
    b++;
}
void wsmaller()
{

    b+=1+(nb-b);
}
 void gotoxy(int x,int y)
 {
   coord.X=x;
 coord.Y=y;
 SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),coord);
 }
void delay(unsigned int mseconds)
{
   clock_t time;
   time=mseconds +clock();
   while(time>clock());

}




