#include"NeuralNetwork_battle.h"
PyObject* PyModule_battle;
PyObject* PyFunction_battle;
PyObject* PyInput_battle;
PyObject* PyResult_battle;

void
InitalNeuralNetwork_battle()
{
	Py_Initialize();
	//多线程支持
	//PyEval_InitThreads();
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('./')");
	if (!Py_IsInitialized())
	{
		system("pause");
	}
	PyModule_battle = PyImport_ImportModule("Machine_Learning_CNN_G");
	if (PyModule_battle == NULL)
	{
		system("pause");
	}
	PyFunction_battle = PyObject_GetAttrString(PyModule_battle, "GetValue");
}

int NeuralNetWork_battle(statestack input)
{
	PyInput_battle = PyTuple_New(75);
	for (int s = 0; s < 3; s++)
	{
		for (int y = 0; y < 5; y++)
		{
			for (int x = 0; x < 5; x++)
			{
				PyTuple_SetItem(PyInput_battle, s * 25 + y * 5 + x, Py_BuildValue("i", input.cb_battle[s].set[x][y]));
				//  be used to test python to c;
				//	PyTuple_SetItem(PyInput_battle, s * 25 + y * 5 + x, Py_BuildValue("i", 0));
			}
		}
	}
	PyResult_battle = PyObject_CallFunctionObjArgs(PyFunction_battle, PyInput_battle, NULL);
	//PyErr_PrintEx(1);
	if (PyResult_battle == NULL)
	{
		system("pause");
	}
	int result = PyLong_AsLong(PyResult_battle);
	Py_DECREF(PyInput_battle);
	return result;
}

void Py_Rename_battle(string tem)
{
	PyRun_SimpleString("import os");
}
void DestroyNeuralNetWork_battle()
{
	Py_Finalize();
}
