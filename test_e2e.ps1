# End-to-end test script
Write-Host "Testing Report Generator API..." -ForegroundColor Green

# Test 1: Health check
Write-Host "`n1. Testing health endpoint..." -ForegroundColor Yellow
$health = Invoke-RestMethod -Uri "http://localhost:8000/api/health"
Write-Host "   Status: $($health.status)" -ForegroundColor Cyan

# Test 2: Validation
Write-Host "`n2. Testing validation endpoint..." -ForegroundColor Yellow
$validateBody = @{
    config = @{
        project_info = @{
            title = "E2E Test Report"
            description = "Testing the complete pipeline"
            students = @(
                @{
                    name = "Test User"
                    id = "12345"
                }
            )
            university = "Test University"
        }
        report_profile = @{
            report_type = "project_report"
            language = "vi"
        }
        technical_data = @{
            algorithms = @("BFS", "DFS", "A*")
            technologies = @("Python", "React", "TypeScript")
        }
    }
} | ConvertTo-Json -Depth 10

$validation = Invoke-RestMethod -Uri "http://localhost:8000/api/validate" -Method Post -Body $validateBody -ContentType "application/json"
Write-Host "   Valid: $($validation.valid)" -ForegroundColor Cyan
Write-Host "   Errors: $($validation.errors.Count)" -ForegroundColor Cyan
Write-Host "   Warnings: $($validation.warnings.Count)" -ForegroundColor Cyan

# Test 3: Generate report
Write-Host "`n3. Testing generate endpoint..." -ForegroundColor Yellow
$job = Invoke-RestMethod -Uri "http://localhost:8000/api/generate" -Method Post -Body $validateBody -ContentType "application/json"
Write-Host "   Job ID: $($job.job_id)" -ForegroundColor Cyan
Write-Host "   Status: $($job.status)" -ForegroundColor Cyan

# Test 4: Poll job status
Write-Host "`n4. Polling job status..." -ForegroundColor Yellow
$maxAttempts = 30
$attempt = 0
do {
    Start-Sleep -Seconds 1
    $status = Invoke-RestMethod -Uri "http://localhost:8000/api/jobs/$($job.job_id)"
    $attempt++
    Write-Host "   Attempt $attempt - Status: $($status.status) - Progress: $($status.progress)%" -ForegroundColor Cyan
} while ($status.status -eq "running" -or $status.status -eq "pending" -and $attempt -lt $maxAttempts)

if ($status.status -eq "completed") {
    Write-Host "`n5. Job completed successfully!" -ForegroundColor Green
    Write-Host "   File ID: $($status.file_id)" -ForegroundColor Cyan
    
    # Test 5: Download file
    Write-Host "`n6. Testing download endpoint..." -ForegroundColor Yellow
    $downloadPath = "test_e2e_report.docx"
    Invoke-WebRequest -Uri "http://localhost:8000/api/download/$($status.file_id)" -OutFile $downloadPath -UseBasicParsing
    if (Test-Path $downloadPath) {
        $fileSize = (Get-Item $downloadPath).Length
        Write-Host "   Downloaded: $downloadPath ($fileSize bytes)" -ForegroundColor Green
    }
} elseif ($status.status -eq "failed") {
    Write-Host "`n5. Job failed!" -ForegroundColor Red
    Write-Host "   Error: $($status.error)" -ForegroundColor Red
} else {
    Write-Host "`n5. Job timed out!" -ForegroundColor Red
}

Write-Host "`nAll tests completed!" -ForegroundColor Green
