TRAIN_DATA = [
    (
        "김민수 매니저가 담당하는 베타는 내부 민감 프로젝트이다.",
        {"entities": [(14, 19, "PROJECT_NAME"), (0, 3, "PROJECT_MANAGER")]} 
    ),
    (
        "데이터 통합 프로젝트는 2025년 3월 1일부터 2025년 3월 1일까지 진행된다.",
        {"entities": [(0, 6, "PROJECT_NAME"), (13, 24, "PROJECT_DATE")]} 
    ),
    (
        "프로젝트 관리는 매우 중요한 업무입니다.",
        {"entities": []}
    ),
    (
        "델타 프로젝트는 2027년 2월 28일부터 2026년 12월 31일까지 진행된다.",
        {"entities": [(0, 2, "PROJECT_NAME"), (9, 21, "PROJECT_DATE"), (24, 37, "PROJECT_DATE")]} 
    ),
    (
        "우리는 좋은 팀 환경을 만들기 위해 노력하고 있습니다.",
        {"entities": []}
    ),
    (
        "전략기획팀 주관으로 진행되는 클라우드 전환의 책임자는 정하늘이다.",
        {"entities": [(16, 23, "PROJECT_NAME"), (30, 33, "PROJECT_MANAGER"), (0, 5, "ORG_INTERNAL")]} 
    ),
    (
        "보안개발팀 주관으로 진행되는 감마의 책임자는 최유진이다.",
        {"entities": [(16, 18, "PROJECT_NAME"), (25, 28, "PROJECT_MANAGER"), (0, 5, "ORG_INTERNAL")]} 
    ),
    (
        "회사의 목표는 고객 만족을 최우선으로 하는 것입니다.",
        {"entities": []}
    ),
    (
        "프로젝트 차세대 보안는 총 예산 22억 원으로 정하늘 PM이 담당한다.",
        {"entities": [(5, 11, "PROJECT_NAME"), (26, 29, "PROJECT_MANAGER"), (18, 23, "PROJECT_BUDGET")]} 
    ),
    (
        "프로젝트 데이터 통합는 총 예산 22억 원으로 정하늘 PM이 담당한다.",
        {"entities": [(5, 11, "PROJECT_NAME"), (26, 29, "PROJECT_MANAGER"), (18, 23, "PROJECT_BUDGET")]} 
    ),
    (
        "이 문서는 공개 가능한 일반 정보입니다.",
        {"entities": []}
    ),
    (
        "델타 프로젝트의 예산은 5억 원으로 책정되었다.",
        {"entities": [(0, 2, "PROJECT_NAME"), (13, 17, "PROJECT_BUDGET")]} 
    ),
    (
        "프로젝트 코드명 레드존는 내부 문서에서만 사용된다.",
        {"entities": [(9, 14, "PROJECT_TERM")]} 
    ),
    (
        "업무 효율성을 높이기 위해 새로운 도구를 도입했습니다.",
        {"entities": []}
    ),
    (
        "감마 프로젝트는 2026년 1월 1일부터 2027년 2월 28일까지 진행된다.",
        {"entities": [(0, 2, "PROJECT_NAME"), (9, 20, "PROJECT_DATE"), (23, 35, "PROJECT_DATE")]} 
    ),
    (
        "프로젝트 차세대 보안는 총 예산 12억 원으로 김민수 PM이 담당한다.",
        {"entities": [(5, 11, "PROJECT_NAME"), (26, 29, "PROJECT_MANAGER"), (18, 23, "PROJECT_BUDGET")]} 
    ),
    (
        "팀 회의는 매주 목요일에 진행됩니다.",
        {"entities": []}
    ),
    (
        "R&D혁신팀 주관으로 진행되는 델타의 책임자는 윤도현이다.",
        {"entities": [(17, 19, "PROJECT_NAME"), (26, 29, "PROJECT_MANAGER"), (0, 6, "ORG_INTERNAL")]} 
    ),
    (
        "프로젝트 코드명 내부등급A는 내부 문서에서만 사용된다.",
        {"entities": [(9, 14, "PROJECT_TERM")]} 
    ),
    (
        "고객 만족도는 우리의 최고 우선순위입니다.",
        {"entities": []}
    ),
    (
        "프로젝트 AI 분석는 총 예산 22억 원으로 윤도현 PM이 담당한다.",
        {"entities": [(5, 10, "PROJECT_NAME"), (25, 28, "PROJECT_MANAGER"), (17, 22, "PROJECT_BUDGET")]} 
    ),
    (
        "베타 프로젝트의 예산은 22억 원으로 책정되었다.",
        {"entities": [(0, 2, "PROJECT_NAME"), (13, 18, "PROJECT_BUDGET")]} 
    ),
    (
        "안녕하세요. 어떻게 도와드릴까요?",
        {"entities": []}
    ),
    (
        "송지훈 매니저가 담당하는 내부 감사는 내부 민감 프로젝트이다.",
        {"entities": [(14, 19, "PROJECT_NAME"), (0, 3, "PROJECT_MANAGER")]} 
    ),
    (
        "이 기능은 모든 사용자에게 공개되어 있습니다.",
        {"entities": []}
    ),
    (
        "오메가 프로젝트의 책임자는 이준혁이다.",
        {"entities": [(0, 3, "PROJECT_NAME"), (14, 17, "PROJECT_MANAGER")]} 
    ),
    (
        "당사는 2025년부터 새로운 서비스를 제공하고 있습니다.",
        {"entities": []}
    ),
    (
        "마케팅팀 주관으로 진행되는 브랜드 혁신의 담당자는 박미진이다.",
        {"entities": [(16, 21, "PROJECT_NAME"), (26, 29, "PROJECT_MANAGER"), (0, 5, "ORG_INTERNAL")]} 
    ),
    (
        "프로젝트 스마트팩토리는 총 예산 50억 원으로 책정되었다.",
        {"entities": [(5, 14, "PROJECT_NAME"), (23, 28, "PROJECT_BUDGET")]} 
    ),
    (
        "팀원들과의 협력이 성공의 열쇠입니다.",
        {"entities": []}
    ),
    (
        "알파 프로젝트는 2026년 6월부터 2027년 5월까지 진행될 예정이다.",
        {"entities": [(0, 3, "PROJECT_NAME"), (9, 19, "PROJECT_DATE"), (22, 32, "PROJECT_DATE")]} 
    ),
    (
        "회의실은 3층에 위치하고 있습니다.",
        {"entities": []}
    ),
    (
        "재무팀 주관으로 진행되는 시스템 통합의 책임자는 서동욱이다.",
        {"entities": [(16, 21, "PROJECT_NAME"), (26, 29, "PROJECT_MANAGER"), (0, 5, "ORG_INTERNAL")]} 
    ),
    (
        "프로젝트 클라우드 마이그레이션는 총 예산 30억 원으로 진행된다.",
        {"entities": [(5, 17, "PROJECT_NAME"), (26, 31, "PROJECT_BUDGET")]} 
    ),
    (
        "업무 프로세스 개선을 위한 피드백을 환영합니다.",
        {"entities": []}
    ),
    (
        "감시팀에서 진행하는 보안강화 프로젝트의 PM은 홍길동이다.",
        {"entities": [(15, 20, "PROJECT_NAME"), (25, 28, "PROJECT_MANAGER"), (0, 4, "ORG_INTERNAL")]} 
    ),
    (
        "프로젝트 코드명 블루싸이는 극비 프로젝트이다.",
        {"entities": [(9, 14, "PROJECT_TERM")]} 
    ),
    (
        "우리 회사는 여러 나라에서 사업을 하고 있습니다.",
        {"entities": []}
    ),
    (
        "장비팀 주관으로 진행되는 하드웨어 업그레이드의 책임자는 강민철이다.",
        {"entities": [(16, 23, "PROJECT_NAME"), (28, 31, "PROJECT_MANAGER"), (0, 5, "ORG_INTERNAL")]} 
    ),
    (
        "프로젝트 모바일 앱 개발는 총 예산 15억 원으로 진행 중이다.",
        {"entities": [(5, 14, "PROJECT_NAME"), (23, 28, "PROJECT_BUDGET")]} 
    ),
    (
        "이는 공개 문서이므로 누구나 접근할 수 있습니다.",
        {"entities": []}
    ),
    (
        "데이터팀에서 담당하는 AI 학습 모델의 매니저는 최우성이다.",
        {"entities": [(15, 21, "PROJECT_NAME"), (25, 28, "PROJECT_MANAGER"), (0, 4, "ORG_INTERNAL")]} 
    ),
    (
        "프로젝트 코드명 자금조달은 외부 공개 금지이다.",
        {"entities": [(9, 14, "PROJECT_TERM")]} 
    ),
    (
        "새로운 정책에 대해 더 알고 싶으신가요?",
        {"entities": []}
    ),
    (
        "엔지니어링팀 주관으로 진행되는 인프라 현대화의 담당자는 이영준이다.",
        {"entities": [(16, 23, "PROJECT_NAME"), (28, 31, "PROJECT_MANAGER"), (0, 7, "ORG_INTERNAL")]} 
    ),
    (
        "프로젝트 블록체인 파일럿은 총 예산 8억 원으로 책정되었다.",
        {"entities": [(5, 15, "PROJECT_NAME"), (24, 28, "PROJECT_BUDGET")]} 
    ),
    (
        "문제 해결을 위한 새로운 방법론을 제시했습니다.",
        {"entities": []}
    ),
    (
        "운영팀에서 추진하는 자동화 프로젝트의 책임자는 한정수이다.",
        {"entities": [(13, 18, "PROJECT_NAME"), (23, 26, "PROJECT_MANAGER"), (0, 4, "ORG_INTERNAL")]} 
    ),
    (
        "프로젝트 코드명 프론티어는 특별 관리 대상이다.",
        {"entities": [(9, 14, "PROJECT_TERM")]} 
    ),
    (
        "직원들의 역량 개발이 중요한 과제입니다.",
        {"entities": []}
    ),
    (
        "영업팀 주관으로 진행되는 시장 확대의 매니저는 조금희이다.",
        {"entities": [(16, 21, "PROJECT_NAME"), (26, 29, "PROJECT_MANAGER"), (0, 4, "ORG_INTERNAL")]} 
    ),
    (
        "프로젝트 HR 시스템은 총 예산 25억 원으로 진행된다.",
        {"entities": [(5, 12, "PROJECT_NAME"), (21, 26, "PROJECT_BUDGET")]} 
    ),
    (
        "고객 피드백은 우리의 개선 방향을 결정합니다.",
        {"entities": []}
    ),
    (
        "법무팀에서 담당하는 규정 정비 프로젝트의 PM은 김도엽이다.",
        {"entities": [(16, 21, "PROJECT_NAME"), (26, 29, "PROJECT_MANAGER"), (0, 4, "ORG_INTERNAL")]} 
    ),
    (
        "프로젝트 코드명 실크로드는 국제 협력 프로젝트이다.",
        {"entities": [(9, 14, "PROJECT_TERM")]} 
    ),
    (
        "회사의 이익 창출이 모든 활동의 목표입니다.",
        {"entities": []}
    ),
    (
        "콘텐츠팀 주관으로 진행되는 디지털 마케팅의 담당자는 박준호이다.",
        {"entities": [(16, 22, "PROJECT_NAME"), (27, 30, "PROJECT_MANAGER"), (0, 5, "ORG_INTERNAL")]} 
    ),
    (
        "프로젝트 보안감시는 총 예산 18억 원으로 책정되었다.",
        {"entities": [(5, 11, "PROJECT_NAME"), (20, 25, "PROJECT_BUDGET")]} 
    ),
    (
        "새로운 기술 도입으로 업무 효율이 향상되었습니다.",
        {"entities": []}
    ),
    (
        "인사팀에서 진행하는 복지 확대 프로젝트의 책임자는 이소영이다.",
        {"entities": [(14, 19, "PROJECT_NAME"), (24, 27, "PROJECT_MANAGER"), (0, 4, "ORG_INTERNAL")]} 
    ),
    (
        "프로젝트 코드명 골든게이트는 제한된 접근만 허용된다.",
        {"entities": [(9, 14, "PROJECT_TERM")]} 
    ),
    (
        "사회 공헌 활동도 우리의 경영 철학 중 하나입니다.",
        {"entities": []}
    ),
    (
        "품질팀 주관으로 진행되는 서비스 개선의 매니저는 정재운이다.",
        {"entities": [(16, 21, "PROJECT_NAME"), (26, 29, "PROJECT_MANAGER"), (0, 4, "ORG_INTERNAL")]} 
    ),
    (
        "프로젝트 공급망 최적화는 총 예산 35억 원으로 진행 중이다.",
        {"entities": [(5, 13, "PROJECT_NAME"), (22, 27, "PROJECT_BUDGET")]} 
    ),
    (
        "사무직과 현장직의 협력이 성공적으로 이루어지고 있습니다.",
        {"entities": []}
    )
]