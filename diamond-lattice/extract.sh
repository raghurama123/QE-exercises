for file in lattice_0*/diamond.out; do
    a=$( grep 'lattice parameter (alat)' $file | awk '{print $5}' )
    Energy=$( grep '!    total energy              =  ' $file | awk '{print $5}' )
    echo $a','$Energy
done
