import heapq


def solution(jobs):
    jobs.sort()

    heap = []
    answer = 0
    cur_time = 0

    completed_jobs = 0
    job_id = 0

    while completed_jobs < len(jobs):
        while job_id < len(jobs) and jobs[job_id][0] <= cur_time:
            requested_time, duration = jobs[job_id]
            heapq.heappush(heap, (duration, requested_time))
            job_id += 1

        if heap:
            duration, requested_time, = heapq.heappop(heap)
            cur_time += duration
            answer += cur_time - requested_time
            completed_jobs += 1
            continue
        cur_time = jobs[job_id][0]

    return answer // len(jobs)
