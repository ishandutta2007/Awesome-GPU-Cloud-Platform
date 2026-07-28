<div align="center">
  <img src="assets/banner.svg" alt="Awesome GPU Cloud Platform Banner" />
</div>

# Awesome-GPU-Cloud-Platform

<meta name="description" content="Curated list of the best GPU Cloud Platforms, GPU-as-a-Service, and open-source GPU cluster managers for AI training and inference.">
<meta name="keywords" content="GPU Cloud, AI, ML, Deep Learning, H100, A100, NVIDIA, Kubernetes, GPU-as-a-Service, vast.ai, runpod, coreweave">
## Top GPU Cloud Platforms Ecosystem
**Curated List of SaaS Products & Open-Source GitHub Projects**
*Focused on GPU-as-a-Service, AI/ML Training & Inference, Bare-Metal Clusters & Cost-Efficient Compute*
**Last updated: July 2026**

This repository tracks notable **SaaS platforms** and **open-source projects** for **GPU Cloud Platforms**. These tools provide on-demand or reserved access to NVIDIA (and other) GPUs for training, fine-tuning, inference, and high-performance computing, often undercutting traditional hyperscalers on price while offering AI-optimized networking, storage, and developer experience.

**Examples** include CoreWeave, Lambda, Crusoe Cloud, RunPod, Vast.ai, Fluidstack, Modal, Nebius AI Cloud, TensorDock, Cudo Compute, Voltage Park, Hyperbolic, and Hyperstack (the category leaders and popular alternatives).

**Open-source emphasis**: This section is heavily expanded with every major active project for self-hosting, multi-cloud orchestration, GPU cluster management, Kubernetes operators, and decentralized marketplaces — ideal for AI labs, researchers, startups, and developers building transparent, cost-optimized, or private GPU infrastructure.

Contributions welcome! Open a PR to add/update entries. Keep descriptions factual and link to official sites.

## 📚 Table of Contents
- [SaaS/Hosted Platforms](#saas-hosted-platforms)
- [Open-Source GitHub Projects](#open-source-github-projects)
- [How to Contribute](#how-to-contribute)
- [Disclaimer](#disclaimer)

## ☁️ SaaS/Hosted Platforms

### Core Platforms (GPU Cloud / Neoclouds)
- **[CoreWeave](https://www.coreweave.com/)**  
  Large-scale NVIDIA GPU cloud purpose-built for AI training and inference; bare-metal clusters, InfiniBand, Kubernetes-native (CKS), enterprise SLAs.

- **[Lambda](https://lambda.ai/)** (Lambda Labs)  
  Developer- and researcher-friendly GPU cloud with transparent pricing, on-demand and reserved H100/A100 clusters, strong academic ties.

- **[Crusoe Cloud](https://www.crusoe.ai/)** (Crusoe Energy)  
  Sustainable GPU cloud powered by stranded/flared gas and renewables; vertically integrated data centers focused on energy efficiency and large contiguous clusters.

- **[RunPod](https://www.runpod.io/)**  
  Developer-centric GPU marketplace with pods, serverless endpoints, per-second billing, wide GPU selection (consumer to H100/H200), and strong community cloud.

- **[Vast.ai](https://vast.ai/)**  
  Peer-to-peer GPU marketplace offering some of the lowest prices; rent from independent hosts or data centers with interruptible/spot options.

- **[Fluidstack](https://www.fluidstack.io/)**  
  Distributed GPU cloud combining private capacity and marketplace aggregation; supports large private-cloud deployments for frontier AI labs.

- **[Modal](https://modal.com/)**  
  Serverless GPU platform for Python functions and AI workloads; scale-to-zero, per-second billing, zero infrastructure management.

- **[Nebius AI Cloud](https://nebius.com/)** (Nebius AI)  
  European/sovereign-focused GPU cloud with managed Kubernetes, Slurm, full ML stack, and competitive H100/H200 pricing.

- **[TensorDock](https://tensordock.com/)**  
  Budget-oriented GPU cloud with transparent pricing and good reliability for individuals and small teams.

- **[Cudo Compute](https://www.cudocompute.com/)**  
  GPU cloud marketplace and provider offering on-demand instances with free egress options and competitive rates.

- **[Voltage Park](https://www.voltagepark.com/)**  
  Large-scale H100-focused GPU cloud targeting foundation-model training clusters with competitive on-demand pricing.

- **[Hyperbolic](https://hyperbolic.xyz/)**  
  AI-native compute platform emphasizing agent hosting and open-source model support.

- **[Hyperstack](https://www.hyperstack.cloud/)**  
  On-demand GPU cloud (H100, A100, L40S) with per-minute billing, European presence, and developer-friendly access.

## 🛠️ Open-Source GitHub Projects

- **[vLLM](https://github.com/vllm-project/vllm)** [![GitHub stars](https://img.shields.io/github/stars/vllm-project/vllm?style=social&color=white)](https://github.com/vllm-project/vllm/stargazers)  
  High-throughput, memory-efficient open-source LLM inference and serving engine with PagedAttention, continuous batching, and tensor/pipeline parallelism — widely used as the backend for self-hosted GPU clouds.

- **[SGLang](https://github.com/sgl-project/sglang)** [![GitHub stars](https://img.shields.io/github/stars/sgl-project/sglang?style=social&color=white)](https://github.com/sgl-project/sglang/stargazers)  
  Fast open-source serving framework for large language and multimodal models; strong structured generation and high-performance inference backend.

- **[SkyPilot](https://github.com/skypilot-org/skypilot)** [![GitHub stars](https://img.shields.io/github/stars/skypilot-org/skypilot?style=social&color=white)](https://github.com/skypilot-org/skypilot/stargazers)  
  Open-source framework to run, manage, and scale AI workloads across any infrastructure (Kubernetes, Slurm, 20+ clouds including Lambda/RunPod/Vast.ai/Nebius/Crusoe, on-prem). Unifies compute into one “sky”, optimizes for cost and availability, supports spot recovery.

- **[GPUStack](https://github.com/gpustack/gpustack)** [![GitHub stars](https://img.shields.io/github/stars/gpustack/gpustack?style=social&color=white)](https://github.com/gpustack/gpustack/stargazers)  
  Open-source GPU cluster manager for high-performance AI model serving (vLLM, SGLang, TensorRT-LLM) and on-demand SSH-accessible GPU instances. Multi-cluster, multi-vendor (NVIDIA, AMD, Apple Silicon, Ascend, etc.), OpenAI-compatible APIs.

- **[NVIDIA GPU Operator](https://github.com/NVIDIA/gpu-operator)** [![GitHub stars](https://img.shields.io/github/stars/NVIDIA/gpu-operator?style=social&color=white)](https://github.com/NVIDIA/gpu-operator/stargazers)  
  Kubernetes operator that automates installation, configuration, and lifecycle management of NVIDIA drivers, container runtime, device plugin, DCGM monitoring, and MIG on GPU nodes.

- **[Kubeflow Trainer](https://github.com/kubeflow/trainer)** [![GitHub stars](https://img.shields.io/github/stars/kubeflow/trainer?style=social&color=white)](https://github.com/kubeflow/trainer/stargazers)  
  Kubernetes-native distributed training and LLM fine-tuning platform supporting PyTorch, JAX, DeepSpeed, Hugging Face, MPI, and more, with multi-node multi-GPU orchestration.

- **[NVIDIA DeepOps](https://github.com/NVIDIA/deepops)** [![GitHub stars](https://img.shields.io/github/stars/NVIDIA/deepops?style=social&color=white)](https://github.com/NVIDIA/deepops/stargazers)  
  Ansible-based toolkit for rapidly deploying and managing GPU clusters with Kubernetes or Slurm, including drivers, networking, monitoring, and best practices for DGX and commodity hardware.

- **[KAI Scheduler](https://github.com/NVIDIA/KAI-scheduler)** [![GitHub stars](https://img.shields.io/github/stars/NVIDIA/KAI-scheduler?style=social&color=white)](https://github.com/NVIDIA/KAI-scheduler/stargazers)  
  Open-source Kubernetes-native scheduler optimized for large-scale AI/ML workloads; supports GPU sharing, elastic jobs, DRA, and high-throughput scheduling across thousands of nodes.

- **[Akash Network](https://github.com/akash-network)** [![GitHub stars](https://img.shields.io/github/stars/akash-network/node?style=social&color=white)](https://github.com/akash-network/node/stargazers)  
  Decentralized open-source cloud marketplace (Cosmos SDK) enabling peer-to-peer GPU and compute rental with reverse-auction pricing.

### Additional Strong Open-Source Options
- **NVIDIA DCGM / DCGM Exporter** — Data Center GPU Manager and Prometheus exporter for GPU health, utilization, and metrics.
- **Kueue** — Kubernetes-native job queueing system for batch and ML workloads, improving GPU utilization.
- **Karpenter** — Open-source Kubernetes node autoscaler with strong GPU instance support (especially on AWS).
- **OpenCost** — Open-source cost monitoring and attribution for Kubernetes, including GPU resources.
- **Ray** (Anyscale open-source core) — Distributed computing framework frequently used for multi-GPU training and inference orchestration.
- **Tinkerbell / OpenStack Ironic / MAAS** — Open-source bare-metal provisioning tools useful for building private GPU clouds.
- **LLMKube / similar operators** — Kubernetes operators for heterogeneous self-hosted LLM inference across NVIDIA, AMD, and Apple Silicon.
- Community decentralized marketplaces and agents (e.g., various DePIN GPU rental projects on GitHub) for peer-to-peer compute sharing.
- Many **Prometheus + Grafana + DCGM** dashboards and **InfluxDB** stacks for GPU observability.

**Frameworks for building custom systems**: Combine **SkyPilot** or **GPUStack** with **NVIDIA GPU Operator**, **Kubernetes + Kueue**, **vLLM/SGLang**, **DeepOps**, and monitoring stacks (Prometheus/Grafana/DCGM) to create private or multi-cloud GPU platforms equivalent to commercial neoclouds.

## 🤝 How to Contribute
1. Fork the repo.
2. Add/edit entries in `README.md` (follow existing format).
3. Include: name, link, 1–2 sentence description, and whether it's SaaS or open-source.
4. Submit PR with a short explanation.

Star the repo if you find it useful!

## ⚠️ Disclaimer
- This is a **community-curated** list — not exhaustive and not an endorsement.
- GPU cloud usage involves significant cost, data-transfer, and compliance considerations (export controls, data residency, etc.).
- Self-hosted open-source solutions require proper security hardening, driver management, networking (InfiniBand/RoCE), and operational expertise for production reliability.

---
**Made for AI researchers, ML engineers, startups, and infrastructure teams.**  
Let's make high-performance GPU compute more open, cost-efficient, and accessible.
