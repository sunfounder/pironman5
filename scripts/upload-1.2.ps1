[CmdletBinding()]
param(
    [Parameter(Mandatory=$false, HelpMessage="目标合并分支")]
    [string]$targetBranch = "main",
    [Parameter(Mandatory=$false, HelpMessage="版本号，用于生成tag")]
    [string]$version
)

$list = @(
    "base",
    "max",
    "mini",
    "main"
)

function Merge-And-Upload {
    param(
        [string]$name,
        [string]$targetBranch
    )

    Write-Host "Merging and uploading $name with target branch: $targetBranch"

    # Merge the branch
    git checkout $name
    git merge $targetBranch

    # Upload the merged branch
    git push origin $name
}

foreach ($name in $list) {
    Merge-And-Upload -name $name -targetBranch $targetBranch
}

# 如果提供了版本号，创建并上传tag
if ($version) {
    $tagName = "$version"
    Write-Host "Creating and pushing tag: $tagName"
    git tag $tagName
    git push origin $tagName
}
