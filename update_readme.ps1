$readme = "README.md"
$content = Get-Content $readme -Raw

# 1. Banner
$banner = "<div align=`"center`">`n  <img src=`"assets/banner.svg`" alt=`"Awesome GPU Cloud Platform Banner`" />`n</div>`n`n"
$content = $banner + $content
Set-Content $readme $content -NoNewline
git add .
git commit -m "added banner"

# 2. Emojis
$content = $content -replace "## Table of Contents", "## 📚 Table of Contents"
$content = $content -replace "## SaaS/Hosted Platforms", "## ☁️ SaaS/Hosted Platforms"
$content = $content -replace "## Open-Source GitHub Projects", "## 🛠️ Open-Source GitHub Projects"
$content = $content -replace "## How to Contribute", "## 🤝 How to Contribute"
$content = $content -replace "## Disclaimer", "## ⚠️ Disclaimer"
Set-Content $readme $content -NoNewline
git add .
git commit -m "added emojis"

# 3. SEO
$seo = "`n<meta name=`"description`" content=`"Curated list of the best GPU Cloud Platforms, GPU-as-a-Service, and open-source GPU cluster managers for AI training and inference.`">`n<meta name=`"keywords`" content=`"GPU Cloud, AI, ML, Deep Learning, H100, A100, NVIDIA, Kubernetes, GPU-as-a-Service, vast.ai, runpod, coreweave`">`n"
$content = $content -replace "# Awesome-GPU-Cloud-Platform", "# Awesome GPU Cloud Platform - AI/ML Compute Guide$seo"
Set-Content $readme $content -NoNewline
git add .
git commit -m "seo optimised"

# 4 & 5. Badges
$badges_left = "<a href=`"https://github.com/ishandutta2007/Awesome-Awesome-Awesome`"><img src=`"https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github`" alt=`"Awesome`"/></a><a href=`"https://discord.gg/jc4xtF58Ve`"><img src=`"https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white`" alt=`"Discord`" /></a>"
$badges_right = "<a href=`"https://github.com/ishandutta2007`"><img alt=`"GitHub followers`" src=`"https://img.shields.io/github/followers/ishandutta2007?label=Follow`" /></a>"

$badge_placeholder = "<p align=`"center`">`n  $badges_left`n</p>`n"
$content = $content.Replace($seo, $seo + $badge_placeholder)
Set-Content $readme $content -NoNewline
git add .
git commit -m "badges to left added"

$content = $content.Replace($badges_left, $badges_left + $badges_right)
Set-Content $readme $content -NoNewline
git add .
git commit -m "badges to right added"

# 6. Star history
$star_history = @"

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
"@
$content = $content + $star_history
Set-Content $readme $content -NoNewline
git add .
git commit -m "star history added"

# 7. fixed star plot
$content = $content.Replace("chartrepos", "chart?repos")
Set-Content $readme $content -NoNewline
git add .
git commit -m "fixed star plot"

# 8. invalid awesome link fixed
$content = $content.Replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
Set-Content $readme $content -NoNewline
git add .
git commit -m "invalid awesome link fixed"
