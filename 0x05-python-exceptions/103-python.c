#include <Python.h>

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @pob: A PyObject byte object.
 */
void print_python_bytes(PyObject *pob)
{
	Py_ssize_t size, i;
	PyBytesObject *bytes = (PyBytesObject *)pob;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(pob->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)pob)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)pob)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)pob)->ob_size + 1;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @pob: A PyObject float object.
 */
void print_python_float(PyObject *pob)
{
	char *buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)pob;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(pob->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}

/**
 * print_python_list - Prints basic info about Python lists.
 * @pob: A PyObject list object.
 */
void print_python_list(PyObject *pob)
{
	Py_ssize_t size, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)pob;
	PyVarObject *var = (PyVarObject *)pob;

	size = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(pob->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}
