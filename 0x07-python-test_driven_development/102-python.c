#include "Python.h"

/**
 * print_python_string - Prints info about Python strings.
 * @pob: A PyObject string object.
 */
void print_python_string(PyObject *pob)
{
	long int length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(pob->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	lgt = ((PyASCIIObject *)(pob))->lgt;

	if (PyUnicode_IS_COMPACT_ASCII(pob))
		printf("  type: compact ascii\n");

	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", lgt);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(pob, &lgt));
}
