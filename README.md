# bb-graph-mpi
 Branch and Bound Graph Algorithm with MPI Python

### Special thanks goes to
*   https://stackoverflow.com/a/54907810
*   https://duongtrungnghia.wordpress.com/2017/03/28/install-mpi4py-on-windows-10/
*   https://mpi4py.readthedocs.io/en/stable/install.html#requirements

### Requirements
*   Python 3.x
*   PiP
*   Both of the [Files downloaded](https://www.microsoft.com/en-us/download/confirmation.aspx?id=100593) from here, namely msmpisdk.msi and msmpisetup.exe

### How to make this sh*t run
1.  Install the requirements above
2.  Add the installation folder for each Program in your path variable
>   Go to search and type environment and select first thing like "Edit System Variable"

>   You will find the Environment Variables button in bottom right

>   Add to the path variable the installation folders (for me they were 

>>   C:\Program Files\Microsoft MPI\Bin 

>>   C:\Program Files (x86)\Microsoft SDKs\MPI\
3.  Install the requirements in [requirements.txt](./requirements.txt)
```
pip install -r requirements.txt
```
as a matter of fact you can add an environment to make things more professional

Navigate to the project folder
```
cd /where/i/made/this/project
```
You can make your Python Script to make some Parallel Computing like the one in sample.py

```py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print('this process rank is ', rank)

```

and then start the parallel computing
```powershell
mpiexec -n 5 py sample.py
```

Should output something like this
```powershell
[(your_environment)/your/folder] mpiexec -n 5 py sample.py
My rank is  4
My rank is  1
My rank is  3
My rank is  0
My rank is  2
```
## Good luck