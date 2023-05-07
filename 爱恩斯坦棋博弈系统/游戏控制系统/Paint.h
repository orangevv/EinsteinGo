#pragma once
#include<graphics.h>
#include<string>
#include<fstream>
#include<iostream>
#include<ctime>
#include<windows.h>
#include<cstdlib>

using std::string;
struct chessboard
{
	int set[5][5];
};

class Paint
{
public:
	Paint();
	~Paint();
	void PaintChessboard();
	void PaintElememt();
	void PaintDisplayElememt(bool first);
	void PaintModeDispaly(bool AItoAI);
	void DiceDispaly(int dice);
	void PaintChessman(chessboard cb);
	bool IsLtTrue();
	bool IsLtFalse();
	bool RunningMode();
	bool RandomLtTrue();
	int GetDice();
	int RandDice();
	int GetMovingChessman();
	int GetWay();
	char GetMode();
	bool IsBackMode();
	bool IsContinueBack();
	int NumberChessman(int x, int y);
};

