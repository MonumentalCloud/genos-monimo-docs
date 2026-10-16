현재 확인한 Flowise 변경 소스에서 직접 참조하는 GenOS·스킬 환경변수 이름과 읽는 위치입니다. 배포 환경의 실제 값·비밀정보는 포함하지 않습니다. 이 목록은 환경변수를 새로 설정하라는 권장이 아닙니다. 기본값·유효값·적용 범위는 해당 기능 설명과 소스의 해석 함수를 확인하세요. 프로세스별 설정 차이도 확인해야 합니다.

## GENOS_A2A_COOPERATIVE_AGENT_IDS

- [buildAgentflow.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/server/src/utils/buildAgentflow.ts)

## GENOS_A2A_COOPERATIVE_PAUSE

- [buildAgentflow.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/server/src/utils/buildAgentflow.ts)

## GENOS_AGENTFLOW_NODE_LOG

- [buildAgentflow.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/server/src/utils/buildAgentflow.ts)

## GENOS_AGENTFLOW_TRACE_JOIN

- [handler.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/handler.ts)

## GENOS_BOOT_MIGRATIONS

- [DataSource.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/server/src/DataSource.ts)
- [genosRuntime.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/server/src/genosRuntime.ts)
- [index.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/server/src/index.ts)

## GENOS_CHECKPOINT_TTL_SEC

- [genosSubjectScope.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/server/src/utils/genosSubjectScope.ts)

## GENOS_DEV_TOKEN

- [Agent.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/agentflow/Agent/Agent.ts)
- [GenosA2A.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/agentflow/GenosA2A/GenosA2A.ts)
- [MncRerankAgentflow.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/agentflow/MncRerankAgentflow/MncRerankAgentflow.ts)
- [MonimoAgent.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/agentflow/MonimoAgent/MonimoAgent.ts)
- [ChatMnc.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/chatmodels/ChatMnc/ChatMnc.ts)
- [MncOpenAIEmbedding.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/embeddings/MncOpenAIEmbedding/MncOpenAIEmbedding.ts)
- [MncRerankRetriever.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/retrievers/MncRerankRetriever/MncRerankRetriever.ts)
- [GenOSLongTermMemory.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/tools/GenOSMemory/GenOSLongTermMemory.ts)
- [GenosMCP.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/tools/MCP/GenosMCP/GenosMCP.ts)
- [SkillPipeline.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/vectorstores/DeepSearfing/SkillPipeline.ts)
- [index.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/server/src/services/nodes/index.ts)

## GENOS_LLM_MAX_RETRIES

- [genosLlmDefaults.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/genosLlmDefaults.ts)

## GENOS_LLM_TIMEOUT_MS

- [genosLlmDefaults.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/genosLlmDefaults.ts)

## GENOS_OVERLAY_REV

- [genosRuntime.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/server/src/genosRuntime.ts)

## GENOS_PYTHON_BIN

- [utils.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/utils.ts)

## GENOS_SECFILTER_MODE

- [Retriever.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/agentflow/Retriever/Retriever.ts)
- [RetrieverTool.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/tools/RetrieverTool/RetrieverTool.ts)
- [skillBodyAccess.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/genos/skillBodyAccess.ts)
- [buildAgentflow.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/server/src/utils/buildAgentflow.ts)

## GENOS_SHARED_SCHEMA_GUARD

- [genosRuntime.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/server/src/genosRuntime.ts)
- [index.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/server/src/routes/index.ts)

## GENOS_SKILL_SEARCH_CACHE_MAX_MB

- [skillSearchCache.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/genos/skillSearchCache.ts)

## GENOS_SKILL_SEARCH_CACHE_TTL_MS

- [skillSearchCache.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/genos/skillSearchCache.ts)

## GENOS_SKILL_SEARCH_MAX_PER_TURN

- [skillGate.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/skillGate.ts)

## GENOS_SKILL_SELECT_WOULD_HIT_TTL_MS

- [skillSelectorMode.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/genos/skillSelectorMode.ts)

## GENOS_STOCK_LLM_TRACEPARENT

- [genosTrace.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/genosTrace.ts)

## GENOS_STREAM_EXECUTED_DATA

- [toClientExecution.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/server/src/utils/toClientExecution.ts)

## GENOS_TEST_SYSTEM_RECEIPTS

- [testSystemReceipt.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/genos/testSystemReceipt.ts)

## GENOS_WORKFLOW_EDIT_LOCK

- [index.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/server/src/routes/index.ts)

## GENOS_WORKFLOW_ID

- [S3StorageProvider.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/storage/S3StorageProvider.ts)
- [ControllerServiceUtils.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/server/src/genos-oss/utils/ControllerServiceUtils.ts)
- [genosRuntime.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/server/src/genosRuntime.ts)

## SKILLS_POLICY_ENABLED

- [DeepSearfing.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/vectorstores/DeepSearfing/DeepSearfing.ts)
- [SkillPipeline.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/vectorstores/DeepSearfing/SkillPipeline.ts)
- [skillBodySources.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/genos/skillBodySources.ts)
