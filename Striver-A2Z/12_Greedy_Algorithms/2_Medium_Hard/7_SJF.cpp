
#include <iostream>
#include <set>
using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);

    int n, temp, i, j;
    int total_time_cpu = 0;
    float total_waiting_time = 0, total_turnaround_time = 0, cpu_idle_time = 0;

    cout << "Enter no of Process:" << endl;
    cin >> n;

    int arrival_time[n], burst_time[n], turn_around_time[n], waiting_time[n], process_seq[n];

    // Taking Input
    for (i = 0; i < n; i++)
    {
        cout << "\nEnter Arrival time " << i + 1 << " :";
        cin >> arrival_time[i];
        cout << "\nEnter Burst time " << i + 1 << " :";
        cin >> burst_time[i];
        process_seq[i] = i + 1;
    }

    // Displaying Input
    cout << "\n\n Before Scheduling:";
    cout << "\n ProcessId \t ArrivalTime \t BurstTime\n";
    for (i = 0; i < n; i++)
    {
        cout << process_seq[i] << "\t\t" << arrival_time[i] << "\t\t" << burst_time[i] << endl;
    }

    // Sort According to Burst Time
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n - 1; j++)
        {
            if (burst_time[j] > burst_time[j + 1])
            {
                temp = arrival_time[j];
                arrival_time[j] = arrival_time[j + 1];
                arrival_time[j + 1] = temp;

                temp = burst_time[j];
                burst_time[j] = burst_time[j + 1];
                burst_time[j + 1] = temp;

                temp = process_seq[j];
                process_seq[j] = process_seq[j + 1];
                process_seq[j + 1] = temp;
            }
        }
    }

    // Getting Minimum Arrival Time
    int first_arrive = arrival_time[0], first_index_arrive = 0;

    for (i = 0; i < n; i++)
    {
        if (first_arrive > arrival_time[i])
        {
            first_arrive = arrival_time[i];
            first_index_arrive = i;
        }
    }

    // Task:
    //    1) Take the first arrival job and execute it
    //    2)  From the next job check if it is arrived or
    //        not if arrived execute that process

    // Waiting Time = TurnAroundTime  - BurstTime
    // TurnAroundTime = ExitTime  - ArrivalTime

    // Taking first arrival job
    int process = n;
    i = 0; // first_index_arrive;
    total_time_cpu = first_arrive;

    cout << "\n\n firs" << first_arrive << " " << first_index_arrive;

    cout << "\n\n After Sorting:" << endl;
    for (i = 0; i < n; i++)
    {
        cout << process_seq[i] << "\t\t" << arrival_time[i] << "\t\t" << burst_time[i] << "\t\t" << endl;
    }

    // Completed Process Set
    set<int> completed_process;

    cout << "\n i:" << i;
    cout << "\n ProcessID \t ArrivalTime \t BurstTime \t TurnAroundTime \t WaitingTime \n";
    int flag = 1;

    while (process != 0)
    {
        // If Process Arrived Run it
        if (arrival_time[i] <= total_time_cpu && completed_process.find(i) == completed_process.end())
        {
            total_time_cpu += burst_time[i];
            turn_around_time[i] = total_time_cpu - arrival_time[i];
            waiting_time[i] = turn_around_time[i] - burst_time[i];

            total_waiting_time += waiting_time[i];
            total_turnaround_time += turn_around_time[i];

            // Once Process Complete decrement it
            process--;
            completed_process.insert(i);

            cout << process_seq[i] << "\t\t" << arrival_time[i] << "\t\t" << burst_time[i] << "\t\t" << turn_around_time[i] << "\t\t\t" << waiting_time[i] << endl;
            i = 0;
            continue;
        }

        if (i >= n - 1)
        {
            i = 0;
        }
        else
        {
            i++;
        }
    }

    cout << "\n\n Average Waiting Time: " << total_waiting_time / n;
    cout << "\n\n Average TurnAround Time: " << total_turnaround_time / n << endl;

    return 0;
}