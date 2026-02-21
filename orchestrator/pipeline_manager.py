from orchestrator.agent_controller import AgentController

class PipelineManager:
    def __init__(self):
        self.controller = AgentController()

    def generate_report(self, pdf_path, query=None):
        return self.controller.run_full_pipeline(pdf_path, query)
