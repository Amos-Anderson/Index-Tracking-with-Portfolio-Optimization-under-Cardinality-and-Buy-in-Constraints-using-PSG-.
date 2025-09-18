# PSG Optimization set up

allowExternal = True
suppressMessages = False

# Problem Statement
problem_name = "problem_index_tracking"

problem_statement = "minimize \n\
  max_risk(matrix_inmmax) \n\
Constraint: <= 50 \n\
  cardn_pos(0.01, matrix_ksi) \n\
Constraint: <= 0 \n\
  buyin_pos(0.01, matrix_ksibuy) \n\
Constraint: <= 100 \n\
  linear(matrix_ksi) \n\
  +variable(trcost) \n\
Constraint: <= 94 \n\
  variable(trcost) \n\
Constraint: <= 0 \n\
  -variable(trcost) \n\
  +0.01*polynom_abs(matrix_ksipol) \n\
  +100*cardn_pos(0.01, matrix_ksipol) \n\
  +100*cardn_neg(0.01, matrix_ksipol) \n\
Box: >= 0 \n\
Solver: CAR, precision = 3, stages = 3"

problem_dictionary_indx_track = {'problem_name':problem_name, 'problem_statement':problem_statement,
                        'matrix_inmmax' : track_port_matrix,
                        'matrix_ksi' : cardn_constraint, 
                        'matrix_ksibuy' : buyin_constraint,
                        'matrix_ksipol' : poly_constraint}

result = psg.psg_solver(problem_dictionary_indx_track, allowExternal, suppressMessages)