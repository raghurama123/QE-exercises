import os
import subprocess

def write_inp(dirname,a):

    #print(dirname, a)

    inpfile=open('diamond.in','w')

    inpfile.write(' &control \n')
    inpfile.write(' calculation = \'scf\' \n')
    inpfile.write(' restart_mode = \'from_scratch\' \n')
    inpfile.write(' prefix = \'diamond\' \n')
    inpfile.write(' pseudo_dir = \'../../pseudo/\' \n')
    inpfile.write(' outdir = \''+dirname+'\' \n')
    inpfile.write(' / \n')
    inpfile.write('\n')

    inpfile.write(' &system \n')
    inpfile.write(' celldm(1) = {:8.3f} \n'.format(a))
    inpfile.write(' ibrav = 2 \n')
    inpfile.write(' nat = 2 \n')
    inpfile.write(' ntyp = 1 \n')
    inpfile.write(' ecutwfc = 90 \n')
    inpfile.write(' / \n')
    inpfile.write('\n')

    inpfile.write(' &electrons \n')
    inpfile.write(' mixing_beta = 0.2 \n')
    inpfile.write(' conv_thr =  1e-8 \n')
    inpfile.write(' diagonalization = \'david\' \n')
    inpfile.write(' diago_thr_init = 1e-4 \n')
    inpfile.write(' / \n')
    inpfile.write('\n')

    inpfile.write(' ATOMIC_SPECIES \n')
    inpfile.write(' C  12.000  C.pbe-n-kjpaw_psl.1.0.0.UPF \n')
    inpfile.write(' K_POINTS automatic \n')
    inpfile.write(' 4 4 4   0 0 0 \n')
    inpfile.write('\n')

    inpfile.write(' ATOMIC_POSITIONS crystal \n')
    inpfile.write(' C   0.12500000000000   0.12500000000000   0.12500000000000 \n')
    inpfile.write(' C   0.87500000000000   0.87500000000000   0.87500000000000 \n')
    inpfile.write('\n')

    inpfile.close()

    return 0

# Define the range of values for 'a'
a_min = 3.0
a_max = 8.0
da    = 0.1

a=a_min
while a < a_max+da:

    dirname='lattice_%05.2f'%a
    os.makedirs(dirname, exist_ok=True)
    os.chdir(dirname)

    pwd = os.getcwd()

    iostat=write_inp(pwd,a)

    runfile=open('run.sh','w')
    #runfile.write(' mpirun -np 2 pw.x < diamond.in      | tee diamond.out \n')
    runfile.write('pw.x < diamond.in      | tee diamond.out \n')
    runfile.close()

    os.system('bash run.sh')

    a = a + da

    os.chdir('../')
