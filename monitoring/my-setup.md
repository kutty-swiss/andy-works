For my **self-hosting setup**, I decided to focus solely on **metrics** and **dashboards** because they provide a lightweight and efficient way to monitor system performance without the added complexity of managing logs and traces. With **Grafana and Prometheus**, I can visualize key resource usage in real-time, ensuring optimal performance while keeping resource overhead minimal. 🚀  


```mermaid
graph TD;
    A[System Metrics] -->|Collected By| B[Node Exporter];
    A -->|Collected By| C[cAdvisor];
    B -->|Sends Data To| D[Prometheus];
    C -->|Sends Data To| D[Prometheus];
    D -->|Data Queried By| E[Grafana];
    E -->|Displays Visualizations| F[User Dashboards];
```

### Dashboards:

#### Example 1: Node Exporter Dashboard  
![Node Exporter Dashboard - Screenshot 1](images/Grafana-a1.png)  
![Node Exporter Dashboard - Screenshot 2](images/Grafana-a2.png)  

#### Example 2: cAdvisor Dashboard  
![cAdvisor Dashboard - Screenshot 1](images/Grafana-b1.png)  
![cAdvisor Dashboard - Screenshot 2](images/Grafana-b2.png)  