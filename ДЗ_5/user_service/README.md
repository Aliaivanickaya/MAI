alisa@MacBook-Pro-Alisa user_service % wrk -t1 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  1 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    27.89ms   10.68ms  98.51ms   89.56%
    Req/Sec   367.30     64.40   440.00     82.00%
  3674 requests in 10.06s, 635.06KB read
Requests/sec:    365.15
Transfer/sec:     63.12KB
alisa@MacBook-Pro-Alisa user_service % wrk -t5 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  5 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    28.33ms   11.19ms 107.50ms   91.56%
    Req/Sec    72.77     14.74   202.00     85.08%
  3638 requests in 10.08s, 628.83KB read
Requests/sec:    360.75
Transfer/sec:     62.36KB
alisa@MacBook-Pro-Alisa user_service % wrk -t10 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    27.65ms   10.81ms 106.58ms   90.42%
    Req/Sec    37.18      7.13    50.00     66.87%
  3713 requests in 10.02s, 641.80KB read
Requests/sec:    370.62
Transfer/sec:     64.06KB

-------------------------------------------------------------------------------------

alisa@MacBook-Pro-Alisa ДЗ_5 % cd user_service             
alisa@MacBook-Pro-Alisa user_service % wrk -t1 -c10 -d10s -s auth.lua http://localhost:8000/users/admin                         
Running 10s test @ http://localhost:8000/users/admin
  1 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    90.65ms   86.85ms 805.28ms   92.81%
    Req/Sec   138.37     46.70   200.00     70.21%
  1315 requests in 10.04s, 227.30KB read
Requests/sec:    131.00
Transfer/sec:     22.64KB
alisa@MacBook-Pro-Alisa user_service % wrk -t5 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  5 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    94.81ms   60.73ms 431.35ms   90.41%
    Req/Sec    23.99      9.77    40.00     68.11%
  1148 requests in 10.08s, 198.43KB read
Requests/sec:    113.93
Transfer/sec:     19.69KB
alisa@MacBook-Pro-Alisa user_service % wrk -t10 -c10 -d10s -s auth.lua http://localhost:8000/users/admin
Running 10s test @ http://localhost:8000/users/admin
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    98.86ms   65.44ms 550.88ms   88.04%
    Req/Sec    12.20      5.47    20.00     56.83%
  1095 requests in 10.05s, 189.27KB read
Requests/sec:    108.91
Transfer/sec:     18.83KB
alisa@MacBook-Pro-Alisa user_service %




Вывод:
С кэшем стало в 3 раза быстрее