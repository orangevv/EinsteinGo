#include "Paint.h"



Paint::Paint()
{
	initgraph(1000, 600);
}


Paint::~Paint()
{
	closegraph();
}

void Paint::PaintChessboard()
{
	setfillcolor(WHITE);
	setlinecolor(BLACK);
	solidrectangle(0, 0, 1000, 600);
	for (int i = 0; i < 6; i++)
	{
		line(50, 100 * i + 50, 550, 100 * i + 50);
		line(100 * i + 50, 50, 100 * i + 50, 550);
	}
	PaintElememt();
}
void Paint::PaintElememt()
{
	line(650, 50, 650, 550);
	line(950, 50, 950, 550);
	for (int i = 0; i < 6; i++)
	{
		line(650, 100 * i + 50, 950, 100 * i + 50);
	}
	LOGFONT f;
	gettextstyle(&f);						// Get the current font settings
	f.lfHeight = 48;						// Set the font height to 48
	_tcscpy(f.lfFaceName, _T("bold"));		// Set the font to "bold" (high-version VC is recommended to use the function of the _tcscpy_s)
	f.lfQuality = ANTIALIASED_QUALITY;
	//settextstyle(24, 0, _T("Consolas"));
	outtextxy(650, 50, "当前行棋方");
	outtextxy(800, 50, "稍后行棋方");

	outtextxy(650, 190, "模式");
	outtextxy(650, 290, "骰子");

	outtextxy(650, 390, "先手方运行时间");
	outtextxy(650, 490, "后手方运行时间");
}
void Paint::PaintDisplayElememt(bool first)
{
	if (first)
	{
		setfillcolor(RED);
		solidrectangle(650,80,700,120);
		setfillcolor(BLUE);
		solidrectangle(800, 80, 850, 120);
	}
	else
	{
		setfillcolor(BLUE);
		solidrectangle(650, 80, 700, 120);
		setfillcolor(RED);
		solidrectangle(800, 80, 850, 120);
	}
}
void Paint::PaintModeDispaly(bool AItoAI)
{
	if(AItoAI)
		outtextxy(800, 190, "机器互弈模式");
	else
		outtextxy(800, 190, "人机对战模式");
}
void Paint::DiceDispaly(int dice)
{
	char s = dice + '0';
	//settextstyle(24, 0, _T("Consolas"));
	outtextxy(850, 290, s);
}
bool Paint::RunningMode()
{
	char tem[2];
	InputBox(tem, 2, "is AI VS AI ?(y/n)");
	if (tem[0] == 'y' || tem[0] == 'Y')
	{
		return true;
	}
	else
	{
		return false;
	}
}
void Paint::PaintChessman(chessboard cb)
{
	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			if (cb.set[i][j] != 0)
			{
				if (cb.set[i][j] > 0)
				{
					setfillcolor(BLUE);
					solidrectangle(100 * i + 51, 100 * j + 51, 100 * i + 149, 100 * j + 149);
				}
				else
				{
					setfillcolor(RED);
					solidrectangle(100 * i + 51, 100 * j + 51, 100 * i + 149, 100 * j + 149);
				}
				outtextxy(100 * i + 51, 100 * j + 51, char(abs(cb.set[i][j]))+'0');
			}
		}
	}
}

bool Paint::IsLtTrue()
{
	char tem[2];
	InputBox(tem, 2, "is AI first?(y/n)");
	if (tem[0] == 'y' || tem[0] == 'Y')
	{
		return true;
	}
	else
	{
		return false;
	}
}
bool Paint::IsLtFalse()
{
	char tem[2];
	InputBox(tem, 2, "is AI second?(y/n)");
	if (tem[0] == 'y' || tem[0] == 'Y')
	{
		return true;
	}
	else
	{
		return false;
	}
}
bool Paint::RandomLtTrue()
{
	LARGE_INTEGER seed;
	QueryPerformanceFrequency(&seed);
	QueryPerformanceCounter(&seed);
	srand(seed.QuadPart); //放入和时间相关的随机数种子。由于种子是随机的，所以随机数也是随机的
	int random = rand()%2; //产生1-很大一个数之间的随机整数
	if (random == 1)
		return true;
	else
		return false;
}


int Paint::GetDice()
{
	char tem[2];
	InputBox(tem, 2, "input the value of dice");
	return (tem[0] - '0');
}
int Paint::RandDice()
{
	int dice;
	LARGE_INTEGER seed;
	QueryPerformanceFrequency(&seed);
	QueryPerformanceCounter(&seed);
	srand(seed.QuadPart);//放入和时间相关的随机数种子。由于种子是随机的，所以随机数也是随机的
	dice = rand()%6+1; //产生1-6很大一个数之间的随机整数
	return dice;
}

int Paint::GetMovingChessman()
{
	char tem[2];
	InputBox(tem, 2, "input the number of moving-chessman");
	return (tem[0] - '0');
}

int Paint::GetWay()
{
	char tem[2];
	InputBox(tem, 2, "input the value of way\n|*|0|    |1|2|\n|2|1|    |0|*|");
	return (tem[0] - '0');
}

char Paint::GetMode()
{
	char tem[2];
	InputBox(tem, 2, "input mode of number chessman(auto-A,manual-M)");
	return tem[0];
}

bool Paint::IsBackMode()
{
	char tem[2];
	InputBox(tem, 2, "do you want to use back-mode(y/n)");
	if (tem[0] == 'y' || tem[0] == 'Y')
	{
		return true;
	}
	else
	{
		return false;
	}
}

bool Paint::IsContinueBack()
{
	char tem[2];
	InputBox(tem, 2, "do you want to back a move(y/n)");
	if (tem[0] == 'y' || tem[0] == 'Y')
	{
		return true;
	}
	else
	{
		return false;
	}
}

int Paint::NumberChessman(int x, int y)
{

	char tem[2];
	setfillcolor(GREEN);
	solidrectangle(100 * x + 51, 100 * y + 51, 100 * x + 149, 100 * y + 149);
	InputBox(tem, 2, "number for light");
	return tem[0] - '0';
}

