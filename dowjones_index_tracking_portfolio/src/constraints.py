cardn_constraint = [headers[:-1], np.full(50, 1.000000000000e+000).reshape(1,50)]
buyin_constraint = [headers[:-1], np.full(50, 1.979012345178e+003).reshape(1,50)]
poly_row1 = np.full(50, 1.000000000000e+000) 
poly_row2 = np.array([
    1.454372622591e+005, 1.979012345178e+005, 1.457831324254e+005,
    1.753012048281e+005, 1.460063899063e+005, 1.321576763202e+005,
    1.551351351246e+005, 1.185383243772e+005, 1.318181819579e+005,
    4.801980192552e+005, *([0.0] * 40)  
])

poly_constraint = [headers[:-1], np.vstack([poly_row1, poly_row2])]