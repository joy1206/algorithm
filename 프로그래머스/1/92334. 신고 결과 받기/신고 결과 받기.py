def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))] 
    report = set(report)
    reported_id = {user: [] for user in id_list} 
    # {'muzi': ['frodo', 'neo'], 'frodo': ['neo'], 'apeach': ['frodo', 'muzi'], 'neo': []} 
    report_count = {user: 0 for user in id_list}
    # {'muzi': 1, 'frodo': 2, 'apeach': 0, 'neo': 2}
 
    for r in report:
        reporter, reported = r.split()
        reported_id[reporter].append(reported)
        report_count[reported] += 1
    
    for i in range(len(id_list)):
        user = id_list[i]
        for reported in reported_id[user]:
            if report_count[reported] >= k :
                answer[i] += 1
    
    return answer