solver = '''\
net: "./train_test.prototxt"
test_iter: 100
test_interval: 1000
base_lr: 0.001
momentum: 0.9
weight_decay: 0.0005
lr_policy: "inv"
gamma: 0.0001
power: 0.75
display: 100
max_iter: 2000
# snapshot: 5000
# snapshot_prefix: "./snapshot"
solver_mode: CPU
'''

with open('./solver.prototxt', 'w') as f:
    f.write(solver)