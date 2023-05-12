# Create ground state density, wavefunction
mpirun -np 2 pw.x < diamond.in      | tee diamond.out 

# Prepare data for making band structure plot
mpirun -np 2 pw.x < diamond_band.in | tee diamond_band.out

# Post-process the band structure data
bands.x < diamond_bands_pp.in       | tee diamond_bands_pp.out

