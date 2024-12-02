from datetime import datetime

# def calculate_progress(start_date, end_date):
#     # 시작일과 종료일을 datetime 형식으로 변환
#     start = datetime.strptime(start_date, "%Y/%m/%d")
#     end = datetime.strptime(end_date, "%Y/%m/%d")
#     today = datetime.today()

#     # 총 기간 계산
#     total_duration = (end - start).days
#     elapsed_duration = (today - start).days

#     # 진행률 계산 (0~100%)
#     progress = (elapsed_duration / total_duration) * 100
#     return max(0, min(progress, 100))  # 0% 미만, 100% 초과 방지

# # 진행률 계산
# start_date = "2024/08/26"
# end_date = "2025/01/24"
# progress = calculate_progress(start_date, end_date)

# # README.md 파일 업데이트
# with open("README.md", "r") as file:
#     readme_content = file.readlines()

# # 진행률 바를 찾아서 업데이트
# for i, line in enumerate(readme_content):
#     if "![Progress Bar]" in line:
#         readme_content[i] = f"![Progress Bar](https://progress-bar.dev/{int(progress)}) {progress:.2f}% complete\n"

# # 변경된 내용을 다시 README.md 파일에 씀
# with open("README.md", "w") as file:
#     file.writelines(readme_content)
