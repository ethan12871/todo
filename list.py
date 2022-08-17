学习计划

2021.11.27 https://www.cnblogs.com/qiuhom-1874/ 学习他的博客 
     12.11 确认eks系统是否组件k8s 评分，驱逐的到么
     13.25 https://wiki.eryajf.net/pages/2104.html 学习这个博客 
     12.27 如何快速排查机器负载过高的问题 https://blog.csdn.net/qq_41342577/article/details/105029607

2022 1.6 https://www.cnblogs.com/wanson/articles/13769373.html js 学习

2022 1.6 阿里云服务网格 在ASM中通过EnvoyFilter添加HTTP响应头 https://www.alibabacloud.com/help/zh/doc-detail/158520.htm 
2022 4.2 linux几种软件的安装总结 
2022.7.13 https://www.cnblogs.com/qiuhom-1874/p/14161950.html kube-proxy会创建iptables规则直接捕获到达Clusterip和port的流量，并将其重定向至当前service对象的后端pod资源 
2022.7.15 https://www.cnblogs.com/qiuhom-1874/p/14130540.html 对于service来说，在k8s上创建service，从本质上讲就是创建iptables或ipvs规则；
2022.8.9 jsonpath https://www.cnblogs.com/Zhan-W/p/15650408.html


2022.08.15
http响应头安全策略（nginx版） https://blog.csdn.net/liulangdewoniu/article/details/116459468
Web 前端安全问题 - XSS、CSRF、界面操作劫持 https://blog.csdn.net/lhz_333/article/details/123580912
2022.08.17
DaemonSet控制器的主要作用是管理守护进程类的Pod，通常用于在每个节点需要运行一个这样的Pod场景；比如我们要收集日志到es中，我们就可以使用这种控制器在每个节点上运行一个Pod；
job控制器主要作用是用来运行一个或多个pod来执行任务，当任务执行完成后，自动退出，如果在执行任务过程中pod故障了，job控制器会根据重启策略将其进行重启，直到任务完成pod正常退出；如果重启策略为Never，则pod异常后将不再重启，它会重新创建一个新pod再次执行任务，最后直到任务完成正常退出；
