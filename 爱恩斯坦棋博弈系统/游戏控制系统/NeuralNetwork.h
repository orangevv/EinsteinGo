#pragma once
#include"Paint.h"
#include<Python.h>

//datatsets' pro data struct;
struct statestack
{
	chessboard cb[6];
	chessboard cb_battle[3];
	short int choose;
};
void InitalNeuralNetwork();
int NeuralNetWork(statestack input);
void DestroyNeuralNetWork();
