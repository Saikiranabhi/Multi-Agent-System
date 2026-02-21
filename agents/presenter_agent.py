from output.report_builder import build_report
from utils.logger import logger

class PresenterAgent:
    def run(self, analysis_output):
        logger.info("Building structured multi-page report...")
        report = build_report(analysis_output)
        return report
