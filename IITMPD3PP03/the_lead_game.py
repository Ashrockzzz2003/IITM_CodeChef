N = int(input())
max_lead_1 = 0
max_lead_2 = 0
cumulative_1 = 0
cumulative_2 = 0
for i in range(N):
    arr = list(map(int, input().split(' ')))
    cumulative_1 = arr[0] + cumulative_1
    cumulative_2 = arr[1] + cumulative_2
    if cumulative_1 > cumulative_2:
        lead = cumulative_1 - cumulative_2
        max_lead_1 = max(max_lead_1, lead)
    else:
        lead = cumulative_2 - cumulative_1
        max_lead_2 = max(max_lead_2, lead)
if max_lead_1 > max_lead_2:
    print(1, max_lead_1)
else:
    print(2, max_lead_2)
