import urllib.request
import json

repos = [
    'skypilot-org/skypilot',
    'gpustack/gpustack',
    'NVIDIA/gpu-operator',
    'NVIDIA/deepops',
    'NVIDIA/KAI-scheduler',
    'kubeflow/trainer',
    'vllm-project/vllm',
    'sgl-project/sglang',
    'akash-network/node'
]

results = []
for repo in repos:
    try:
        req = urllib.request.Request(f'https://api.github.com/repos/{repo}', headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            results.append((repo, data.get('stargazers_count', 0)))
    except Exception as e:
        print(f'Error fetching {repo}: {e}')

results.sort(key=lambda x: x[1], reverse=True)
for r in results:
    print(f'{r[0]}: {r[1]}')
