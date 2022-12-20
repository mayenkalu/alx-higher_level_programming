#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p)
{
    if (!PyList_Check(p))
    {
        printf("Error: Invalid PyListObject\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; i++)
    {
        printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        printf("Error: Invalid PyBytesObject\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    printf("[*] Python bytes info\n");
    printf("[*] Size of the Python bytes = %zd\n", size);
    printf("[*] Trying string: %s\n", PyBytes_AsString(p));
    printf("[*] First %zd bytes:", size < 10 ? size : 10);

    for (Py_ssize_t i = 0; i < size && i < 10; i++)
    {
        printf(" %02x", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p)
{
    if (!PyFloat_Check(p))
    {
        printf("Error: Invalid PyFloatObject\n");
        return;
    }

    printf("[*] Python float info\n");
    printf("[*] Value: %f\n", PyFloat_AsDouble(p));
}
