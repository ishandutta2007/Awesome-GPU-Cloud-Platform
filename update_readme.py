import os
import subprocess

def run_cmd(cmd):
    subprocess.run(cmd, shell=True, check=True)

readme = 'README.md'
with open(readme, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Banner
banner = '<div align="center">\n  <img src="assets/banner.svg" alt="Awesome GPU Cloud Platform Banner" />\n</div>\n\n'
content1 = banner + content
with open(readme, 'w', encoding='utf-8') as f:
    f.write(content1)
run_cmd('git add . && git commit -m "added banner"')

# 2. Emojis
content2 = content1.replace("## Table of Contents", "## 📚 Table of Contents")
content2 = content2.replace("## SaaS/Hosted Platforms", "## ☁️ SaaS/Hosted Platforms")
content2 = content2.replace("## Open-Source GitHub Projects", "## 🛠️ Open-Source GitHub Projects")
content2 = content2.replace("## How to Contribute", "## 🤝 How to Contribute")
content2 = content2.replace("## Disclaimer", "## ⚠️ Disclaimer")
with open(readme, 'w', encoding='utf-8') as f:
    f.write(content2)
run_cmd('git add . && git commit -m "added emojis"')

# 3. SEO
seo = '\n<meta name="description" content="Curated list of the best GPU Cloud Platforms, GPU-as-a-Service, and open-source GPU cluster managers for AI training and inference.">\n<meta name="keywords" content="GPU Cloud, AI, ML, Deep Learning, H100, A100, NVIDIA, Kubernetes, GPU-as-a-Service, vast.ai, runpod, coreweave">\n'
content3 = content2.replace("# Awesome-GPU-Cloud-Platform", "# Awesome GPU Cloud Platform - AI/ML Compute Guide" + seo)
with open(readme, 'w', encoding='utf-8') as f:
    f.write(content3)
run_cmd('git add . && git commit -m "seo optimised"')

# 4 & 5. Badges
badges_left = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
badges_right = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'

badge_placeholder = f'<p align="center">\n  {badges_left}\n</p>\n'
content4 = content3.replace(seo, seo + badge_placeholder)
with open(readme, 'w', encoding='utf-8') as f:
    f.write(content4)
run_cmd('git add . && git commit -m "badges to left added"')

content5 = content4.replace(badges_left, badges_left + badges_right)
with open(readme, 'w', encoding='utf-8') as f:
    f.write(content5)
run_cmd('git add . && git commit -m "badges to right added"')

# 6. Star history
star_history = """
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-GPU-Cloud-Platform&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-GPU-Cloud-Platform&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-GPU-Cloud-Platform&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-GPU-Cloud-Platform&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
content6 = content5 + star_history
with open(readme, 'w', encoding='utf-8') as f:
    f.write(content6)
run_cmd('git add . && git commit -m "star history added"')

# 7. fixed star plot
content7 = content6.replace('chartrepos', 'chart?repos')
with open(readme, 'w', encoding='utf-8') as f:
    f.write(content7)
run_cmd('git add . && git commit -m "fixed star plot"')

# 8. invalid awesome link fixed
content8 = content7.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')
with open(readme, 'w', encoding='utf-8') as f:
    f.write(content8)
run_cmd('git add . && git commit -m "invalid awesome link fixed"')
