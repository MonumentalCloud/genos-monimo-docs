변경된 노드의 현재 입력 선언을 원문으로 확인합니다. 아래는 입력 UI의 저장 키·기본값·선택지·표시 조건을 확인하는 참고 자료입니다. 신규 옵션만 추린 목록이 아니며, 실행 처리기의 모든 동작을 대신하지 않습니다. MonimoAgent의 사용법은 [설정 사전](settings.html)을 함께 읽으세요. 런타임 코드 자체는 이 사이트에서 실행되지 않습니다.

## Agent

경로: `flowise/3.0.0/before_install/packages/components/nodes/agentflow/Agent/Agent.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/agentflow/Agent/Agent.ts)

```typescript
[
            {
                label: 'Model',
                name: 'agentModel',
                type: 'asyncOptions',
                loadMethod: 'listModels',
                loadConfig: true
            },
            {
                label: 'Messages',
                name: 'agentMessages',
                type: 'array',
                optional: true,
                acceptVariable: true,
                array: [
                    {
                        label: 'Role',
                        name: 'role',
                        type: 'options',
                        options: [
                            {
                                label: 'System',
                                name: 'system'
                            },
                            {
                                label: 'Assistant',
                                name: 'assistant'
                            },
                            {
                                label: 'Developer',
                                name: 'developer'
                            },
                            {
                                label: 'User',
                                name: 'user'
                            }
                        ]
                    },
                    {
                        label: 'Content',
                        name: 'content',
                        type: 'string',
                        acceptVariable: true,
                        generateInstruction: true,
                        loadPromptCatalog: true,
                        rows: 4
                    }
                ]
            },
            // [GenOS #17908] 프롬프트 변수 바인딩 — 메시지 content 의 {{var}} 에 넣을 값을 노드 레벨 배열로 선언.
            // 치환은 서버(buildAgentflow)가 resolveVariables 이후 단일 패스로 수행한다
            {
                label: 'Prompt Variables',
                name: 'agentPromptVars',
                description: 'Values for {{variable}} tokens in message contents (library prompts included)',
                type: 'array',
                optional: true,
                acceptVariable: true,
                refresh: true,
                array: [
                    {
                        label: 'Variable',
                        name: 'promptVarName',
                        type: 'asyncOptions',
                        loadMethod: 'listPromptVars',
                        refresh: true,
                        freeSolo: true
                    },
                    {
                        label: 'Value',
                        name: 'promptVarValue',
                        type: 'string',
                        acceptVariable: true,
                        acceptNodeOutputAsVariable: true
                    }
                ]
            },
            {
                label: 'OpenAI Built-in Tools',
                name: 'agentToolsBuiltInOpenAI',
                type: 'multiOptions',
                optional: true,
                options: [
                    {
                        label: 'Web Search',
                        name: 'web_search_preview',
                        description: 'Search the web for the latest information'
                    },
                    {
                        label: 'Code Interpreter',
                        name: 'code_interpreter',
                        description: 'Write and run Python code in a sandboxed environment'
                    },
                    {
                        label: 'Image Generation',
                        name: 'image_generation',
                        description: 'Generate images based on a text prompt'
                    }
                ],
                show: {
                    agentModel: 'chatOpenAI'
                }
            },
            {
                label: 'Gemini Built-in Tools',
                name: 'agentToolsBuiltInGemini',
                type: 'multiOptions',
                optional: true,
                options: [
                    {
                        label: 'URL Context',
                        name: 'urlContext',
                        description: 'Extract content from given URLs'
                    },
                    {
                        label: 'Google Search',
                        name: 'googleSearch',
                        description: 'Search real-time web content'
                    },
                    {
                        label: 'Code Execution',
                        name: 'codeExecution',
                        description: 'Write and run Python code in a sandboxed environment'
                    }
                ],
                show: {
                    agentModel: 'chatGoogleGenerativeAI'
                }
            },
            {
                label: 'Anthropic Built-in Tools',
                name: 'agentToolsBuiltInAnthropic',
                type: 'multiOptions',
                optional: true,
                options: [
                    {
                        label: 'Web Search',
                        name: 'web_search_20250305',
                        description: 'Search the web for the latest information'
                    },
                    {
                        label: 'Web Fetch',
                        name: 'web_fetch_20250910',
                        description: 'Retrieve full content from specified web pages'
                    }
                    /*
                    * Not supported yet as we need to get bash_code_execution_tool_result from content:
                    https://docs.claude.com/en/docs/agents-and-tools/tool-use/code-execution-tool#retrieve-generated-files
                    {
                        label: 'Code Interpreter',
                        name: 'code_execution_20250825',
                        description: 'Write and run Python code in a sandboxed environment'
                    }*/
                ],
                show: {
                    agentModel: 'chatAnthropic'
                }
            },
            {
                label: 'Tools',
                name: 'agentTools',
                type: 'array',
                optional: true,
                array: [
                    {
                        label: 'Tool',
                        name: 'agentSelectedTool',
                        type: 'asyncOptions',
                        loadMethod: 'listTools',
                        loadConfig: true
                    },
                    {
                        label: 'Require Human Input',
                        name: 'agentSelectedToolRequiresHumanInput',
                        type: 'boolean',
                        optional: true
                    }
                ]
            },
            {
                label: '서브에이전트(A2A)',
                name: 'agentSubAgents',
                type: 'array',
                optional: true,
                description:
                    '작업을 맡길 A2A 에이전트를 추가합니다. 일반 도구와는 별도로 실행되며, 에이전트 이름과 설명, 주요 기능은 Agent Card에서 자동으로 불러옵니다.',
                array: [
                    {
                        label: '에이전트 소스',
                        name: 'subAgentSource',
                        type: 'options',
                        options: [
                            { label: 'GenOS 내부(에이전트)', name: 'internal' },
                            { label: '외부 URL', name: 'external' }
                        ],
                        default: 'internal'
                    },
                    {
                        label: '서브에이전트',
                        name: 'subAgentCard',
                        type: 'asyncOptions',
                        loadMethod: 'listA2AAgents',
                        description: 'A2A 에이전트로 배포된 워크플로우 중에서 작업을 맡길 대상을 선택합니다.',
                        show: { subAgentSource: 'internal' },
                        optional: true
                    },
                    {
                        label: '외부 에이전트 URL',
                        name: 'subAgentUrl',
                        type: 'string',
                        placeholder: 'https://host/a2a/{card_id}',
                        description: '외부 A2A 서버의 기준 URL을 입력합니다. 에이전트 정보는 해당 서버의 Agent Card에서 불러옵니다.',
                        show: { subAgentSource: 'external' },
                        optional: true
                    },
                    {
                        label: '사용자 확인 요청 전달(HITL)',
                        name: 'subAgentInterrupt',
                        type: 'boolean',
                        default: true,
                        optional: true,
                        description:
                            '서브에이전트가 입력이나 승인을 요청하면 사용자에게 확인 화면을 보여 주고, 답변을 받은 뒤 같은 작업을 이어서 진행합니다. 끄면 확인 요청을 마스터 에이전트가 직접 처리합니다.'
                    },
                    {
                        label: '진행 상황 실시간 중계',
                        name: 'subAgentRelay',
                        type: 'boolean',
                        default: false,
                        optional: true,
                        description:
                            '서브에이전트의 진행 상태와 중간 결과를 채팅 화면에 실시간으로 보여 줍니다. 끄면 최종 결과만 전달합니다.'
                    }
                ]
            },
            {
                label: '서브에이전트 동시 호출 수',
                name: 'subAgentConcurrency',
                type: 'number',
                default: 1,
                description:
                    '한 번에 실행할 수 있는 A2A 서브에이전트의 최대 개수입니다. 1로 설정하면 차례대로 실행하며, 일반 도구 실행에는 영향을 주지 않습니다.',
                optional: true,
                additionalParams: true
            },
            {
                label: '서브에이전트 시스템 프롬프트',
                name: 'subAgentSystemPrompt',
                type: 'string',
                rows: 10,
                default: `A2A 서브에이전트 사용 지침:
1. Agent Card의 설명과 사용자 요청이 실제로 관련 있을 때만 서브에이전트에 작업을 맡긴다. 직접 답할 수 있는 질문에는 호출하지 않는다.
2. 다음 작업에 앞선 결과가 필요하면 결과를 받은 뒤 차례대로 호출한다. 서로 의존하지 않는 작업만 동시에 요청한다.
3. 서브에이전트는 현재 대화나 다른 호출 결과를 볼 수 없다고 가정한다. 전달 메시지만 읽어도 이해할 수 있도록 요청을 완전한 문장으로 작성한다.
4. "방금 목록", "이전 결과", "그 필드", "n번째"처럼 문맥이 필요한 표현은 피하고, 앞 단계에서 확인한 실제 값과 대상, 범위, 원하는 출력 형식을 메시지에 적는다.
5. 목록의 순번을 참조할 때는 항목명을 먼저 확인한 뒤 순번과 이름을 함께 전달한다. 예: "XFolder 검색 조건 필드 목록의 10번째 필드인 ManagerGroupFullPathOID의 설명을 알려줘."
6. 같은 작업을 되풀이하지 않는다. 서브에이전트의 답이 앞서 확인한 값과 다르면 그 차이를 밝히고 명시적으로 확인된 값을 기준으로 답한다.`,
                description:
                    '마스터 에이전트가 서브에이전트를 선택하고 호출 순서를 정할 때 참고하는 지침입니다. 기존 시스템 메시지 뒤에 추가되며, 서브에이전트가 하나 이상 설정된 경우에만 사용합니다.',
                optional: true,
                acceptVariable: true,
                additionalParams: true
            },
            {
                label: '서브에이전트 설명 프롬프트',
                name: 'subAgentToolDescriptionPrompt',
                type: 'string',
                rows: 5,
                default:
                    '이 에이전트에 요청할 때는 전달 메시지만으로 작업을 이해할 수 있게 작성하세요. 앞 단계에서 확인한 실제 값과 대상 범위, 원하는 출력 형식을 포함하고, 목록을 참조할 때는 순번과 실제 항목명을 함께 적으세요.',
                description:
                    'Agent Card 설명 뒤에 덧붙여 마스터 모델에 보여 줄 안내문입니다. 어떤 요청을 어떤 형식으로 전달할지 정할 때 사용하며, 실제 서브에이전트에는 완성된 메시지만 보냅니다.',
                optional: true,
                acceptVariable: true,
                additionalParams: true
            },
            {
                // [GenOS #15904] 한 턴에 도구(MCP 포함)를 과도하게 연속 호출하는 것을 방지.
                // 2.2.3 Conversation Agent 의 Max Iteration 에 대응. 미설정/0 이면 무제한(기존 동작).
                label: 'Max Iterations',
                name: 'agentMaxIterations',
                type: 'number',
                description: 'Agent 가 한 턴에 도구(MCP 포함)를 연속 호출하는 최대 횟수(라운드)입니다. 미설정 또는 0 이면 무제한.',
                optional: true,
                additionalParams: true
            },
            {
                label: 'Knowledge (Document Stores)',
                name: 'agentKnowledgeDocumentStores',
                type: 'array',
                description: 'Give your agent context about different document sources. Document stores must be upserted in advance.',
                client: ['agentflowv2'],
                array: [
                    {
                        label: 'Document Store',
                        name: 'documentStore',
                        type: 'asyncOptions',
                        loadMethod: 'listStores'
                    },
                    {
                        label: 'Describe Knowledge',
                        name: 'docStoreDescription',
                        type: 'string',
                        generateDocStoreDescription: true,
                        placeholder:
                            'Describe what the knowledge base is about, this is useful for the AI to know when and how to search for correct information',
                        rows: 4
                    },
                    {
                        label: 'Return Source Documents',
                        name: 'returnSourceDocuments',
                        type: 'boolean',
                        optional: true
                    },
                    {
                        label: 'Use as Ground Truth',
                        name: 'isGroundTruth',
                        type: 'boolean',
                        optional: true,
                        description:
                            'When enabled, retrieves using the user query and stores the answer + source as ground_truth in trace metadata for evaluation. Not passed to the Agent as a tool.'
                    }
                ],
                optional: true
            },
            {
                label: 'Knowledge (Vector Embeddings)',
                name: 'agentKnowledgeVSEmbeddings',
                type: 'array',
                description: 'Give your agent context about different document sources from existing vector stores and embeddings',
                client: ['agentflowv2'],
                array: [
                    {
                        label: 'Vector Store',
                        name: 'vectorStore',
                        type: 'asyncOptions',
                        loadMethod: 'listVectorStores',
                        loadConfig: true
                    },
                    {
                        label: 'Embedding Model',
                        name: 'embeddingModel',
                        type: 'asyncOptions',
                        loadMethod: 'listEmbeddings',
                        loadConfig: true
                    },
                    {
                        label: 'Knowledge Name',
                        name: 'knowledgeName',
                        type: 'string',
                        placeholder:
                            'A short name for the knowledge base, this is useful for the AI to know when and how to search for correct information'
                    },
                    {
                        label: 'Describe Knowledge',
                        name: 'knowledgeDescription',
                        type: 'string',
                        placeholder:
                            'Describe what the knowledge base is about, this is useful for the AI to know when and how to search for correct information',
                        rows: 4
                    },
                    {
                        label: 'Return Source Documents',
                        name: 'returnSourceDocuments',
                        type: 'boolean',
                        optional: true
                    },
                    {
                        label: 'Use as Ground Truth',
                        name: 'isGroundTruth',
                        type: 'boolean',
                        optional: true,
                        description:
                            'When enabled, retrieves using the user query and stores the answer + source as ground_truth in trace metadata for evaluation. Not passed to the Agent as a tool.'
                    }
                ],
                optional: true
            },
            {
                label: 'Enable Memory',
                name: 'agentEnableMemory',
                type: 'boolean',
                description: 'Enable memory for the conversation thread',
                default: true,
                optional: true
            },
            // [GenOS] 개인화 장기 메모리 자동 recall 주입 (에이전트 도구 호출과 별개, add-only)
            {
                label: '장기 메모리 자동 recall',
                name: 'enableLongTermRecall',
                type: 'boolean',
                description:
                    '켜면 이 Agent 노드 실행(Iteration은 항목별)의 첫 LLM 호출 전에 개인화 장기 메모리를 1회 검색해 주입한다(에이전트 도구 호출과 별개).',
                default: false,
                optional: true
            },
            {
                label: '개인화 메모리 MCP 서버',
                name: 'longTermMemoryMCPServerConfig',
                type: 'asyncOptions',
                loadMethod: 'getMemoryMCP',
                description: '개인화 메모리 MCP 서버 선택',
                show: {
                    enableLongTermRecall: true
                },
                additionalParams: true,
                optional: true
            },
            {
                label: '최대 검색 개수(k)',
                name: 'longTermRecallTopK',
                type: 'number',
                default: 8,
                show: {
                    enableLongTermRecall: true
                },
                additionalParams: true,
                optional: true
            },
            {
                label: '유사도 threshold(min_score)',
                name: 'longTermRecallThreshold',
                type: 'number',
                default: 0,
                description: '이 값 미만 유사도 기억 제외. 0=컷 없음. Weaviate hybrid score 스케일에 맞춰 조정.',
                show: {
                    enableLongTermRecall: true
                },
                additionalParams: true,
                optional: true
            },
            {
                label: '검색 범위',
                name: 'longTermRecallScope',
                type: 'multiOptions',
                options: [
                    { label: '개인(전 서비스 공통)', name: 'personal' },
                    { label: '현재 서비스', name: 'service' }
                ],
                default: ['personal'],
                description: '둘 다 선택하면 개인 메모리와 현재 서비스 메모리를 합쳐 검색합니다.',
                show: {
                    enableLongTermRecall: true
                },
                additionalParams: true,
                optional: true
            },
            {
                label: '검색 컨텍스트 주입 방식',
                name: 'longTermRecallInjectionMode',
                type: 'options',
                options: [
                    {
                        label: '사용자 컨텍스트 (권장)',
                        name: 'userContext',
                        description: '동적 메모리 데이터를 현재 사용자 질문 바로 앞에 낮은 권한의 참고 컨텍스트로 둔다.'
                    },
                    {
                        label: 'System 컨텍스트 (호환)',
                        name: 'system',
                        description: '애플리케이션 system 규칙 뒤에 메모리 컨텍스트를 병합한다.'
                    }
                ],
                default: 'userContext',
                show: {
                    enableLongTermRecall: true
                },
                additionalParams: true,
                optional: true
            },
            {
                label: '검색 컨텍스트 템플릿',
                name: 'longTermRecallContextTemplate',
                type: 'string',
                rows: 10,
                acceptVariable: true,
                default: DEFAULT_LONG_TERM_RECALL_CONTEXT_TEMPLATE,
                description:
                    '안전 안내·구분자 등 recall 프롬프트 전체 설정. {memories} 또는 {memories_json} 필수. 선택값: {query_time}, {count}, {safety}. {memories}는 번호가 붙은 메모리 JSON 목록이다.',
                show: {
                    enableLongTermRecall: true
                },
                additionalParams: true,
                optional: true
            },
            {
                label: 'Memory Type',
                name: 'agentMemoryType',
                type: 'options',
                options: [
                    {
                        label: 'All Messages',
                        name: 'allMessages',
                        description: 'Retrieve all messages from the conversation'
                    },
                    {
                        label: 'Window Size',
                        name: 'windowSize',
                        description: 'Uses a fixed window size to surface the last N messages'
                    },
                    {
                        label: 'Conversation Summary',
                        name: 'conversationSummary',
                        description: 'Summarizes the whole conversation'
                    },
                    {
                        label: 'Conversation Summary Buffer',
                        name: 'conversationSummaryBuffer',
                        description: 'Summarize conversations once token limit is reached. Default to 2000'
                    }
                ],
                optional: true,
                default: 'allMessages',
                show: {
                    agentEnableMemory: true
                }
            },
            {
                label: 'Window Size',
                name: 'agentMemoryWindowSize',
                type: 'number',
                default: '20',
                description: 'Uses a fixed window size to surface the last N messages',
                show: {
                    agentMemoryType: 'windowSize'
                }
            },
            {
                label: 'Max Token Limit',
                name: 'agentMemoryMaxTokenLimit',
                type: 'number',
                default: '2000',
                description: 'Summarize conversations once token limit is reached. Default to 2000',
                show: {
                    agentMemoryType: 'conversationSummaryBuffer'
                }
            },
            {
                label: 'Input Message',
                name: 'agentUserMessage',
                type: 'string',
                description: 'Add an input message as user message at the end of the conversation',
                rows: 4,
                optional: true,
                acceptVariable: true,
                show: {
                    agentEnableMemory: true
                }
            },
            {
                label: 'Return Response As',
                name: 'agentReturnResponseAs',
                type: 'options',
                options: [
                    {
                        label: 'User Message',
                        name: 'userMessage'
                    },
                    {
                        label: 'Assistant Message',
                        name: 'assistantMessage'
                    }
                ],
                default: 'userMessage'
            },
            {
                label: 'JSON Structured Output',
                name: 'agentStructuredOutput',
                description: 'Instruct the Agent to give output in a JSON structured schema',
                type: 'array',
                optional: true,
                acceptVariable: true,
                array: [
                    {
                        label: 'Key',
                        name: 'key',
                        type: 'string'
                    },
                    {
                        label: 'Type',
                        name: 'type',
                        type: 'options',
                        options: [
                            {
                                label: 'String',
                                name: 'string'
                            },
                            {
                                label: 'String Array',
                                name: 'stringArray'
                            },
                            {
                                label: 'Number',
                                name: 'number'
                            },
                            {
                                label: 'Boolean',
                                name: 'boolean'
                            },
                            {
                                label: 'Enum',
                                name: 'enum'
                            },
                            {
                                label: 'JSON Array',
                                name: 'jsonArray'
                            }
                        ]
                    },
                    {
                        label: 'Enum Values',
                        name: 'enumValues',
                        type: 'string',
                        placeholder: 'value1, value2, value3',
                        description: 'Enum values. Separated by comma',
                        optional: true,
                        show: {
                            'agentStructuredOutput[$index].type': 'enum'
                        }
                    },
                    {
                        label: 'JSON Schema',
                        name: 'jsonSchema',
                        type: 'code',
                        placeholder: `{
    "answer": {
        "type": "string",
        "description": "Value of the answer"
    },
    "reason": {
        "type": "string",
        "description": "Reason for the answer"
    },
    "optional": {
        "type": "boolean"
    },
    "count": {
        "type": "number"
    },
    "children": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "string",
                    "description": "Value of the children's answer"
                }
            }
        }
    }
}`,
                        description: 'JSON schema for the structured output',
                        optional: true,
                        hideCodeExecute: true,
                        show: {
                            'agentStructuredOutput[$index].type': 'jsonArray'
                        }
                    },
                    {
                        label: 'Description',
                        name: 'description',
                        type: 'string',
                        placeholder: 'Description of the key'
                    }
                ]
            },
            {
                label: 'Update Flow State',
                name: 'agentUpdateState',
                description: 'Update runtime state during the execution of the workflow',
                type: 'array',
                optional: true,
                acceptVariable: true,
                array: [
                    {
                        label: 'Key',
                        name: 'key',
                        type: 'asyncOptions',
                        loadMethod: 'listRuntimeStateKeys'
                    },
                    {
                        label: 'Value',
                        name: 'value',
                        type: 'string',
                        acceptVariable: true,
                        acceptNodeOutputAsVariable: true
                    }
                ]
            }
        ]
```

## LLM

경로: `flowise/3.0.0/before_install/packages/components/nodes/agentflow/LLM/LLM.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/agentflow/LLM/LLM.ts)

```typescript
[
            {
                label: 'Model',
                name: 'llmModel',
                type: 'asyncOptions',
                loadMethod: 'listModels',
                loadConfig: true
            },
            {
                label: 'Messages',
                name: 'llmMessages',
                type: 'array',
                optional: true,
                acceptVariable: true,
                array: [
                    {
                        label: 'Role',
                        name: 'role',
                        type: 'options',
                        options: [
                            {
                                label: 'System',
                                name: 'system'
                            },
                            {
                                label: 'Assistant',
                                name: 'assistant'
                            },
                            {
                                label: 'Developer',
                                name: 'developer'
                            },
                            {
                                label: 'User',
                                name: 'user'
                            }
                        ]
                    },
                    {
                        label: 'Content',
                        name: 'content',
                        type: 'string',
                        acceptVariable: true,
                        generateInstruction: true,
                        loadPromptCatalog: true,
                        rows: 4
                    }
                ]
            },
            // [GenOS #17908] 프롬프트 변수 바인딩 — 메시지 content 의 {{var}} 에 넣을 값을 노드 레벨 배열로 선언.
            // 치환은 서버(buildAgentflow)가 resolveVariables 이후 단일 패스로 수행한다
            {
                label: 'Prompt Variables',
                name: 'llmPromptVars',
                description: 'Values for {{variable}} tokens in message contents (library prompts included)',
                type: 'array',
                optional: true,
                acceptVariable: true,
                refresh: true,
                array: [
                    {
                        label: 'Variable',
                        name: 'promptVarName',
                        type: 'asyncOptions',
                        loadMethod: 'listPromptVars',
                        refresh: true,
                        freeSolo: true
                    },
                    {
                        label: 'Value',
                        name: 'promptVarValue',
                        type: 'string',
                        acceptVariable: true,
                        acceptNodeOutputAsVariable: true
                    }
                ]
            },
            {
                label: 'Enable Memory',
                name: 'llmEnableMemory',
                type: 'boolean',
                description: 'Enable memory for the conversation thread',
                default: true,
                optional: true
            },
            {
                label: 'Memory Type',
                name: 'llmMemoryType',
                type: 'options',
                options: [
                    {
                        label: 'All Messages',
                        name: 'allMessages',
                        description: 'Retrieve all messages from the conversation'
                    },
                    {
                        label: 'Window Size',
                        name: 'windowSize',
                        description: 'Uses a fixed window size to surface the last N messages'
                    },
                    {
                        label: 'Conversation Summary',
                        name: 'conversationSummary',
                        description: 'Summarizes the whole conversation'
                    },
                    {
                        label: 'Conversation Summary Buffer',
                        name: 'conversationSummaryBuffer',
                        description: 'Summarize conversations once token limit is reached. Default to 2000'
                    }
                ],
                optional: true,
                default: 'allMessages',
                show: {
                    llmEnableMemory: true
                }
            },
            {
                label: 'Window Size',
                name: 'llmMemoryWindowSize',
                type: 'number',
                default: '20',
                description: 'Uses a fixed window size to surface the last N messages',
                show: {
                    llmMemoryType: 'windowSize'
                }
            },
            {
                label: 'Max Token Limit',
                name: 'llmMemoryMaxTokenLimit',
                type: 'number',
                default: '2000',
                description: 'Summarize conversations once token limit is reached. Default to 2000',
                show: {
                    llmMemoryType: 'conversationSummaryBuffer'
                }
            },
            {
                label: 'Input Message',
                name: 'llmUserMessage',
                type: 'string',
                description: 'Add an input message as user message at the end of the conversation',
                rows: 4,
                optional: true,
                acceptVariable: true,
                show: {
                    llmEnableMemory: true
                }
            },
            {
                label: 'Return Response As',
                name: 'llmReturnResponseAs',
                type: 'options',
                options: [
                    {
                        label: 'User Message',
                        name: 'userMessage'
                    },
                    {
                        label: 'Assistant Message',
                        name: 'assistantMessage'
                    }
                ],
                default: 'userMessage'
            },
            {
                label: 'JSON Structured Output',
                name: 'llmStructuredOutput',
                description: 'Instruct the LLM to give output in a JSON structured schema',
                type: 'array',
                optional: true,
                acceptVariable: true,
                array: [
                    {
                        label: 'Key',
                        name: 'key',
                        type: 'string'
                    },
                    {
                        label: 'Type',
                        name: 'type',
                        type: 'options',
                        options: [
                            {
                                label: 'String',
                                name: 'string'
                            },
                            {
                                label: 'String Array',
                                name: 'stringArray'
                            },
                            {
                                label: 'Number',
                                name: 'number'
                            },
                            {
                                label: 'Boolean',
                                name: 'boolean'
                            },
                            {
                                label: 'Enum',
                                name: 'enum'
                            },
                            {
                                label: 'JSON Array',
                                name: 'jsonArray'
                            }
                        ]
                    },
                    {
                        label: 'Enum Values',
                        name: 'enumValues',
                        type: 'string',
                        placeholder: 'value1, value2, value3',
                        description: 'Enum values. Separated by comma',
                        optional: true,
                        show: {
                            'llmStructuredOutput[$index].type': 'enum'
                        }
                    },
                    {
                        label: 'JSON Schema',
                        name: 'jsonSchema',
                        type: 'code',
                        placeholder: `{
    "answer": {
        "type": "string",
        "description": "Value of the answer"
    },
    "reason": {
        "type": "string",
        "description": "Reason for the answer"
    },
    "optional": {
        "type": "boolean"
    },
    "count": {
        "type": "number"
    },
    "children": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "string",
                    "description": "Value of the children's answer"
                }
            }
        }
    }
}`,
                        description: 'JSON schema for the structured output',
                        optional: true,
                        hideCodeExecute: true,
                        show: {
                            'llmStructuredOutput[$index].type': 'jsonArray'
                        }
                    },
                    {
                        label: 'Description',
                        name: 'description',
                        type: 'string',
                        placeholder: 'Description of the key'
                    }
                ]
            },
            {
                label: 'Update Flow State',
                name: 'llmUpdateState',
                description: 'Update runtime state during the execution of the workflow',
                type: 'array',
                optional: true,
                acceptVariable: true,
                array: [
                    {
                        label: 'Key',
                        name: 'key',
                        type: 'asyncOptions',
                        loadMethod: 'listRuntimeStateKeys'
                    },
                    {
                        label: 'Value',
                        name: 'value',
                        type: 'string',
                        acceptVariable: true,
                        acceptNodeOutputAsVariable: true
                    }
                ]
            }
        ]
```

## MncRerankAgentflow

경로: `flowise/3.0.0/before_install/packages/components/nodes/agentflow/MncRerankAgentflow/MncRerankAgentflow.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/agentflow/MncRerankAgentflow/MncRerankAgentflow.ts)

```typescript
[
            {
                label: 'Knowledge (Document Stores)',
                name: 'retrieverKnowledgeDocumentStores',
                type: 'array',
                description: 'Document stores to retrieve information from. Document stores must be upserted in advance.',
                array: [
                    {
                        label: 'Document Store',
                        name: 'documentStore',
                        type: 'asyncOptions',
                        loadMethod: 'listStores'
                    }
                ]
            },
            {
                label: 'Retriever Query',
                name: 'retrieverQuery',
                type: 'string',
                description: '미지정 시 노드로 들어온 입력(사용자 질문)을 사용합니다.',
                placeholder: 'Enter your query here',
                rows: 4,
                optional: true,
                acceptVariable: true
            },
            {
                // 직접 연결 / 서비스 라우터 연결 분기. 'service-router' 선택 시 아래 'Service Router'
                // 셀렉터를 채우면 되고, 'serving' (default) 은 기존처럼 Serving 셀렉터를 사용.
                label: 'Connection Type',
                name: 'connectionType',
                type: 'options',
                options: [
                    { label: 'Direct Serving', name: 'serving' },
                    { label: 'Service Router', name: 'service-router' }
                ],
                default: 'serving'
            },
            {
                label: 'Serving',
                name: 'serving',
                type: 'asyncOptions',
                loadMethod: 'getRerankList',
                optional: true,
                show: { connectionType: 'serving' }
            },
            {
                label: 'Service Router',
                name: 'serviceRouter',
                description: 'Connection Type 이 Service Router 일 때 사용. /service-router/{endpoint} 로 외부 호출.',
                type: 'asyncOptions',
                loadMethod: 'getServiceRouterList',
                optional: true,
                show: { connectionType: 'service-router' }
            },
            {
                label: 'Top K',
                name: 'topK',
                description: 'Number of top results to return after reranking. Default 4.',
                placeholder: '4',
                type: 'number',
                optional: true,
                additionalParams: true
            },
            {
                label: 'Output Format',
                name: 'outputFormat',
                type: 'options',
                options: [
                    { label: 'Text', name: 'text' },
                    { label: 'Text with Metadata', name: 'textWithMetadata' }
                ],
                default: 'text'
            },
            {
                label: 'Update Flow State',
                name: 'retrieverUpdateState',
                description: 'Update runtime state during the execution of the workflow',
                type: 'array',
                optional: true,
                acceptVariable: true,
                array: [
                    {
                        label: 'Key',
                        name: 'key',
                        type: 'asyncOptions',
                        loadMethod: 'listRuntimeStateKeys',
                        freeSolo: true
                    },
                    {
                        label: 'Value',
                        name: 'value',
                        type: 'string',
                        acceptVariable: true,
                        acceptNodeOutputAsVariable: true
                    }
                ]
            }
        ]
```

## MonimoAgent

경로: `flowise/3.0.0/before_install/packages/components/nodes/agentflow/MonimoAgent/MonimoAgent.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/agentflow/MonimoAgent/MonimoAgent.ts)

```typescript
[
            {
                label: '표 데이터 처리', name: 'agentEnableTabular', type: 'boolean', default: false,
                optional: true, additionalParams: true,
description: '도구 결과의 payload[genos-vault]에 명시된 표만 Redis에 같은 루트 턴이 진행·대기하는 동안 보관하고(턴 종료 후 30분 정리 보관), 원본 참조로 불러오기·필터링·배치 계산 도구를 제공합니다. LLM이 행을 다시 작성하지 않습니다. 사용자/대화/루트 턴 범위와 Redis 연결이 필요합니다. 표·Vault 처리를 모두 사용하지 않으려면 이 옵션을 끄고(기본값: 꺼짐), Settings → Vault에서 "Vault 저장 허용 유형"을 비우세요(기본값: 비어 있음). 허용 유형 설정은 전체 Flowise의 모든 워크플로우에 공통 적용되므로, 이 옵션만 꺼도 일반 Vault 처리는 유지될 수 있습니다. Langfuse 추적과 슬롯 기능에는 영향을 주지 않습니다.'
            },
            {
                label: '화이트리스트 수집', name: 'agentCollectWhitelist', type: 'boolean', default: false,
                optional: true, additionalParams: true,
                description: '현재 응답 및 HITL/브릿지 대기 시 선언된 스킬 unmask 유형의 값을 AIM으로 탐지하여 Redis에 저장합니다. 출력은 마스킹하거나 차단하지 않습니다. AIM 인증 정보를 선택하세요.'
            },
            {
                label: 'AIM process_type', name: 'agentAimProcessType', type: 'string', default: 'input',
                optional: true, additionalParams: true, show: { agentCollectWhitelist: true }
            },
            {
                label: 'AIM 제한 시간 (초)', name: 'agentAimTimeout', type: 'number', default: 10,
                optional: true, additionalParams: true, show: { agentCollectWhitelist: true }
            },
            {
                label: 'AIM 입력 변환 JavaScript', name: 'agentAimInputFormatter', type: 'code',
                optional: true, additionalParams: true, show: { agentCollectWhitelist: true },
                description: 'AIM에 보낼 입력만 정리합니다. $input에는 text(기존 입력), content, prompt, component, chainPendingValue, chainSequenceValue, unmaskTypes가 있습니다. 동기 JavaScript로 비어 있지 않은 문자열을 return 하세요. 외부 모듈·네트워크·비동기 작업은 지원하지 않으며 실행 제한은 250ms입니다. 비워 두면 기존 형식을 사용합니다. 오류가 나면 기존 입력으로 수집하고 formatter 상태를 기록합니다. 원본 HITL/브릿지와 AIM 응답은 변경하지 않습니다.',
                codeExample: `const sections = [
  ['응답', $input.content],
  ['사용자 확인 질문', $input.prompt],
  ['사용자 확인 또는 브릿지 데이터', $input.component],
  ['현재 업무 데이터', $input.chainPendingValue ?? $input.chainSequenceValue]
];
return sections
  .filter(([, value]) => value !== undefined && value !== null && value !== '')
  .map(([label, value]) => label + ':\\n' + (typeof value === 'string' ? value : JSON.stringify(value, null, 2)))
  .join('\\n\\n') || $input.text;`
            },
            {
                label: 'Model',
                name: 'agentModel',
                type: 'asyncOptions',
                loadMethod: 'listModels',
                loadConfig: true
            },
            {
                label: '내부 전용 모델 (프라이버시 래치)',
                name: 'agentModelInternal',
                type: 'asyncOptions',
                loadMethod: 'listModels',
                loadConfig: true,
                optional: true,
                description:
                    'external_llm: N 스킬을 선언한 에이전트가 현재 턴의 남은 호출에 사용합니다. 다른 에이전트나 다음 턴에는 적용되지 않습니다. 선언 시 이 값이 비어 있으면 호출은 실패합니다.'
            },
            { label: 'Prompt layouts', name: 'agentPromptLayout', type: 'string', optional: true, additionalParams: true, description: 'Configured in the Prompts tab. Backend-owned runtime values resolve at each model call.' },
            { label: 'Internal tool prompts', name: 'agentInternalToolPrompts', type: 'string', optional: true, additionalParams: true, description: 'Configured in the Prompts tab. Edited internal tool descriptions; tools without an edit keep their built-in description.' },
            {
                label: 'Messages',
                name: 'agentMessages',
                type: 'array',
                optional: true,
                acceptVariable: true,
                array: [
                    {
                        label: 'Role',
                        name: 'role',
                        type: 'options',
                        options: [
                            {
                                label: 'System',
                                name: 'system'
                            },
                            {
                                label: 'Assistant',
                                name: 'assistant'
                            },
                            {
                                label: 'Developer',
                                name: 'developer'
                            },
                            {
                                label: 'User',
                                name: 'user'
                            }
                        ]
                    },
                    {
                        label: 'Content',
                        name: 'content',
                        type: 'string',
                        acceptVariable: true,
                        generateInstruction: true,
                        loadPromptCatalog: true,
                        rows: 4
                    }
                ]
            },
            {
                label: 'OpenAI Built-in Tools',
                name: 'agentToolsBuiltInOpenAI',
                type: 'multiOptions',
                optional: true,
                options: [
                    {
                        label: 'Web Search',
                        name: 'web_search_preview',
                        description: 'Search the web for the latest information'
                    },
                    {
                        label: 'Code Interpreter',
                        name: 'code_interpreter',
                        description: 'Write and run Python code in a sandboxed environment'
                    },
                    {
                        label: 'Image Generation',
                        name: 'image_generation',
                        description: 'Generate images based on a text prompt'
                    }
                ],
                show: {
                    agentModel: 'chatOpenAI'
                }
            },
            {
                label: 'Gemini Built-in Tools',
                name: 'agentToolsBuiltInGemini',
                type: 'multiOptions',
                optional: true,
                options: [
                    {
                        label: 'URL Context',
                        name: 'urlContext',
                        description: 'Extract content from given URLs'
                    },
                    {
                        label: 'Google Search',
                        name: 'googleSearch',
                        description: 'Search real-time web content'
                    },
                    {
                        label: 'Code Execution',
                        name: 'codeExecution',
                        description: 'Write and run Python code in a sandboxed environment'
                    }
                ],
                show: {
                    agentModel: 'chatGoogleGenerativeAI'
                }
            },
            {
                label: 'Anthropic Built-in Tools',
                name: 'agentToolsBuiltInAnthropic',
                type: 'multiOptions',
                optional: true,
                options: [
                    {
                        label: 'Web Search',
                        name: 'web_search_20250305',
                        description: 'Search the web for the latest information'
                    },
                    {
                        label: 'Web Fetch',
                        name: 'web_fetch_20250910',
                        description: 'Retrieve full content from specified web pages'
                    }
                    /*
                    * Not supported yet as we need to get bash_code_execution_tool_result from content:
                    https://docs.claude.com/en/docs/agents-and-tools/tool-use/code-execution-tool#retrieve-generated-files
                    {
                        label: 'Code Interpreter',
                        name: 'code_execution_20250825',
                        description: 'Write and run Python code in a sandboxed environment'
                    }*/
                ],
                show: {
                    agentModel: 'chatAnthropic'
                }
            },
            {
                label: 'Tools',
                name: 'agentTools',
                type: 'array',
                optional: true,
                array: [
                    {
                        label: 'Tool',
                        name: 'agentSelectedTool',
                        type: 'asyncOptions',
                        loadMethod: 'listTools',
                        loadConfig: true
                    },
                    {
                        label: 'Require Human Input',
                        name: 'agentSelectedToolRequiresHumanInput',
                        type: 'boolean',
                        optional: true
                    }
                ]
            },
            {
                label: 'Routing Finalization Policy',
                name: 'agentRoutingPolicy',
                type: 'options',
                options: [{ label: 'Off', name: 'off' }, { label: 'Delegate or Clarify', name: 'delegate-or-clarify' }],
                default: 'off',
                optional: true,
                description: 'Opt-in routing master only: delegate to subagents or request routing clarification; no standalone local final response.'
            },
            {
                label: '사용자 입력 요청 도구(HITL) 사용',
                name: 'agentEnableHitlRequestTool',
                type: 'boolean',
                default: false,
                optional: true,
                description:
                    '모델이 진행에 필요한 정보가 부족하다고 판단하면 request_user_input 도구로 확인 카드(confirm/single-select/multi-select)를 띄우고, 사용자 답변을 받을 때까지 이 노드에서 흐름을 중단합니다. A2A 서브에이전트로 호출될 때는 기존 A2A HITL 계약을 그대로 따릅니다.'
            },
            {
                label: '네이티브 브릿지 호출 도구 사용',
                name: 'agentEnableNativeBridge',
                type: 'boolean',
                default: false,
                optional: true,
                description:
                    '모델이 앱의 네이티브 기능이 필요하다고 판단하면 call_native_bridge 도구로 사용자 기기의 브릿지를 호출하고, 결과를 받을 때까지 이 노드에서 흐름을 중단합니다. 호출 대상을 모델이 고르므로 필요한 에이전트에서만 켜세요. 브릿지 선언이 붙은 MCP 도구는 이 설정과 무관하게 동작합니다.'
            },
            {
                label: '허용 브릿지 서비스',
                name: 'agentNativeBridgeServices',
                type: 'string',
                optional: true,
                placeholder: 'GET_PUSH_SETTING, OPEN_NATIVE',
                description:
                    '위 도구로 호출할 수 있는 서비스를 쉼표로 구분해 제한합니다. 도구를 켠 경우 반드시 지정해야 하며 모델은 목록 밖 서비스를 호출할 수 없습니다.',
                show: {
                    agentEnableNativeBridge: true
                }
            },
            {
                // [GenOS] 절차의 실행 도구(송금 실행 등)를 모델이 직접 부르지 못하게 잠근다.
                // 도구 체인의 on_success 경로만 이 도구들을 부를 수 있다 — 관문(슬롯)을 다
                // 지나기 전에는 실행 지점이 열리지 않는 것을 구조로 보장한다.
                label: '체인 전용 도구',
                name: 'agentChainOnlyTools',
                type: 'asyncMultiOptions',
                loadMethod: 'listBoundToolNames',
                refresh: true,
                optional: true,
                description:
                    '여기 고른 도구는 이 노드에서 모델이 직접 호출할 수 없고 도구 체인(on_success)으로만 실행됩니다. 다른 노드에는 이 설정이 상속되지 않습니다.'
            },
            {
                // [GenOS] 스킬 선언 관문. 켜면 순서가 뒤집힌다 — 모델은 먼저 "어느 안내를 따르는지"
                // 를 doc_id 로 선언해야 하고, 그전에는 스킬 검색 도구를 뺀 모든 도구가 잠긴다.
                // 선언한 문서에 절차 선언(genos-slots)이 있으면 그 절차가 자동으로 열린다 —
                // 모델이 slot_begin 을 부를지 고르는 여지가 없어져 슬롯 잠금이 우회 불가능해진다.
                // 서브에이전트(A2A) 호출도 도구 호출이므로 같은 관문을 지난다.
                //
                // '자동' 은 **이 대화에서 앞 노드가 관문을 운영했는지**를 보고 따른다. 흐름을
                // 검색·선언 노드 / 실행 노드로 쪼갤 때, 뒤 노드마다 이 값을 켜 두는 것을
                // 잊으면 잠금이 조용히 풀린다 — 그 규약을 사람이 지키게 하는 대신 상태로
                // 판정한다. 앞 노드가 관문을 안 썼으면 자동은 끈 것과 같다.
                label: '스킬 선언 필수',
                name: 'agentRequireSkillDeclaration',
                type: 'options',
                options: [
                    { label: '자동 (앞 노드를 따름)', name: 'auto' },
                    { label: '항상 필수', name: 'on' },
                    { label: '사용 안 함', name: 'off' }
                ],
                optional: true,
                default: 'auto',
                description:
                    "모델이 declare_skills 로 따를 안내(doc_id)를 선언하기 전까지 스킬 검색을 제외한 모든 도구(서브에이전트 포함)를 잠급니다. '자동' 은 같은 대화에서 앞 노드가 관문을 운영했으면 이어서 잠그고, 아니면 잠그지 않습니다. '사용 안 함' 은 스킬 검색·선언·슬롯 실행에 참여하지 않으며 앞 노드의 슬롯 상태를 변경하지 않습니다. 체인 전용 도구 제한은 이 노드에서 지정한 도구에만 적용합니다."
            },
            ...skillSearchInputs,
            {
                // 검색 도구만은 선언 전에 열려 있어야 한다 — 닫으면 선언할 doc_id 를 얻을 길이 없다.
                // 노드가 만든 지식베이스 도구는 자동으로 열리고, MCP 검색 도구는 이름을 적어 준다.
                label: '스킬 검색 도구',
                name: 'agentSkillSearchTools',
                type: 'string',
                optional: true,
                placeholder: 'mcp_search_skill',
                description:
                    "쉼표로 구분한 도구 이름. '스킬 선언 필수' 가 켜져 있을 때 선언 전에도 호출할 수 있는 검색 도구입니다(지식베이스 도구는 자동 포함).",
                show: {
                    agentRequireSkillDeclaration: ['auto', 'on', true]
                }
            },
            {
                // [GenOS] 폴백. 검색해도 맞는 안내가 없는 요청은 실제로 있다(안내가 아직 없는
                // 업무, 단순 문의). 그때 관문은 막다른 길이 되어 사용자는 아무 답도 못 받는다.
                // 모델이 declare_fallback 을 선언하면 **여기 적힌 도구만** 열린다 — 봉인된
                // 실행도구는 폴백으로도 열리지 않는다(그게 열리면 관문이 폴백 한 번으로 무의미해진다).
                label: '폴백 도구',
                name: 'agentFallbackTools',
                type: 'asyncMultiOptions',
                // 체인 전용으로 지정한 도구는 폴백으로 열리지 않는다 — 목록에서 아예 뺀다.
                // 고를 수 있는데 조용히 무시되면 흐름 작성자가 이유를 모른다(리뷰 지적).
                loadMethod: 'listFallbackCandidateNames',
                refresh: true,
                optional: true,
                description:
                    '맞는 안내를 찾지 못해 모델이 declare_fallback 을 선언했을 때 열리는 도구입니다. 비워 두면 업무 도구를 열지 않고 안내 없음으로 마무리하는 폴백을 제공합니다. 체인 전용(봉인) 도구는 폴백으로 열리지 않습니다.',
                show: {
                    agentRequireSkillDeclaration: ['auto', 'on', true]
                }
            },
            {
                // [GenOS] 선언을 대조할 기준. 검색 도구가 여러 컬렉션을 물어 올 수 있으므로,
                // "어느 저장소의 문서라야 선언할 수 있는가" 를 흐름이 못 박는다. 비워 두면
                // 대조하지 않는다(기존 동작). 지정하면 출처가 일치하는 문서만 선언 대상이 되고,
                // 출처를 알 수 없는 문서도 제외된다 — 대조할 수 없는 것을 통과시키면 지정이 무의미하다.
                // 저장소는 여러 개 둘 수 있다: 스킬을 도메인별로 나눠 담는 것이 정상이다.
                label: '스킬 DB',
                name: 'agentSkillDb',
                type: 'array',
                optional: true,
                description:
                    '스킬(절차 안내) 문서가 들어 있는 벡터 저장소. 지정하면 이 저장소를 검색하는 도구가 자동으로 붙고, declare_skills 로 선언할 수 있는 문서도 여기서 온 것으로 한정됩니다. 문서에 doc_id 가 실려야 선언이 가능합니다(Metadata Keys 확인).',
                array: [
                    {
                        label: 'Vector Store',
                        name: 'vectorStore',
                        type: 'asyncOptions',
                        loadMethod: 'listVectorStores',
                        loadConfig: true
                    },
                    {
                        label: 'Embedding Model',
                        name: 'embeddingModel',
                        type: 'asyncOptions',
                        loadMethod: 'listEmbeddings',
                        loadConfig: true
                    },
                    {
                        label: '검색 도구 설명',
                        name: 'description',
                        type: 'string',
                        rows: 2,
                        optional: true,
                        placeholder: '이 저장소가 어떤 절차 안내를 담고 있는지 — 모델이 언제 검색할지 판단하는 근거가 됩니다'
                    }
                ],
                show: {
                    agentRequireSkillDeclaration: ['auto', 'on', true]
                }
            },
            {
                // [GenOS] 이 도구는 호출자가 hitl-ui 확장을 광고하면 위 토글과 무관하게 주입된다
                // (A2A 서브가 마스터의 HITL 계약을 따르게 하려는 것). 그런데 그 판단이 호출자 헤더에
                // 달려 있어서, 절차가 정해진 흐름에서도 모델이 임의로 사용자에게 묻게 될 수 있다.
                // 그런 흐름이 확실히 끌 수 있도록 '사용 안 함' 을 둔다.
                label: '사용자 입력 요청 도구 정책',
                name: 'agentHitlRequestToolMode',
                type: 'options',
                options: [
                    {
                        label: '자동',
                        name: 'auto',
                        description: '위 토글이 켜져 있거나, 호출자가 hitl-ui 확장을 광고하면 사용 (기존 동작)'
                    },
                    {
                        label: '항상 사용',
                        name: 'always',
                        description: '호출자와 무관하게 항상 사용'
                    },
                    {
                        label: '사용 안 함',
                        name: 'never',
                        description: '호출자가 확장을 광고해도 사용하지 않음. 절차가 정해진 흐름에 쓴다'
                    }
                ],
                default: 'auto',
                optional: true,
                description:
                    '모델이 스스로 사용자에게 묻는 것을 허용할지 정합니다. 기본값 자동은 기존 동작과 같습니다.'
            },
            {
                label: '서브에이전트(A2A)',
                name: 'agentSubAgents',
                type: 'array',
                optional: true,
                description:
                    '작업을 맡길 A2A 에이전트를 추가합니다. 일반 도구와는 별도로 실행되며, 에이전트 이름과 설명, 주요 기능은 Agent Card에서 자동으로 불러옵니다.',
                array: [
                    {
                        label: '에이전트 소스',
                        name: 'subAgentSource',
                        type: 'options',
                        options: [
                            { label: 'GenOS 내부(에이전트)', name: 'internal' },
                            { label: '외부 URL', name: 'external' }
                        ],
                        default: 'internal'
                    },
                    {
                        label: '서브에이전트',
                        name: 'subAgentCard',
                        type: 'asyncOptions',
                        loadMethod: 'listA2AAgents',
                        description: 'A2A 에이전트로 배포된 워크플로우 중에서 작업을 맡길 대상을 선택합니다.',
                        show: { subAgentSource: 'internal' },
                        optional: true
                    },
                    {
                        label: '외부 에이전트 URL',
                        name: 'subAgentUrl',
                        type: 'string',
                        placeholder: 'https://host/a2a/{card_id}',
                        description: '외부 A2A 서버의 기준 URL을 입력합니다. 에이전트 정보는 해당 서버의 Agent Card에서 불러옵니다.',
                        show: { subAgentSource: 'external' },
                        optional: true
                    },
                    {
                        label: '사용자 확인 요청 전달(HITL)',
                        name: 'subAgentInterrupt',
                        type: 'boolean',
                        default: true,
                        optional: true,
                        description:
                            '서브에이전트가 입력이나 승인을 요청하면 사용자에게 확인 화면을 보여 주고, 답변을 받은 뒤 같은 작업을 이어서 진행합니다. 끄면 확인 요청을 마스터 에이전트가 직접 처리합니다.'
                    },
                    {
                        label: '진행 상황 실시간 중계',
                        name: 'subAgentRelay',
                        type: 'boolean',
                        default: false,
                        optional: true,
                        description:
                            '서브에이전트의 진행 상태와 중간 결과를 채팅 화면에 실시간으로 보여 줍니다. 끄면 최종 결과만 전달합니다.'
                    }
                ]
            },
            {
                label: '서브에이전트 동시 호출 수',
                name: 'subAgentConcurrency',
                type: 'number',
                default: 1,
                description:
                    '한 번에 실행할 수 있는 A2A 서브에이전트의 최대 개수입니다. 1로 설정하면 차례대로 실행하며, 일반 도구 실행에는 영향을 주지 않습니다.',
                optional: true,
                additionalParams: true
            },
            {
                label: '서브에이전트 시스템 프롬프트',
                name: 'subAgentSystemPrompt',
                type: 'string',
                rows: 10,
                default: `A2A 서브에이전트 사용 지침:
1. Agent Card의 설명과 사용자 요청이 실제로 관련 있을 때만 서브에이전트에 작업을 맡긴다. 직접 답할 수 있는 질문에는 호출하지 않는다.
2. 다음 작업에 앞선 결과가 필요하면 결과를 받은 뒤 차례대로 호출한다. 서로 의존하지 않는 작업만 동시에 요청한다.
3. 서브에이전트는 현재 대화나 다른 호출 결과를 볼 수 없다고 가정한다. 전달 메시지만 읽어도 이해할 수 있도록 요청을 완전한 문장으로 작성한다.
4. "방금 목록", "이전 결과", "그 필드", "n번째"처럼 문맥이 필요한 표현은 피하고, 앞 단계에서 확인한 실제 값과 대상, 범위, 원하는 출력 형식을 메시지에 적는다.
5. 목록의 순번을 참조할 때는 항목명을 먼저 확인한 뒤 순번과 이름을 함께 전달한다. 예: "XFolder 검색 조건 필드 목록의 10번째 필드인 ManagerGroupFullPathOID의 설명을 알려줘."
6. 같은 작업을 되풀이하지 않는다. 서브에이전트의 답이 앞서 확인한 값과 다르면 그 차이를 밝히고 명시적으로 확인된 값을 기준으로 답한다.`,
                description:
                    '마스터 에이전트가 서브에이전트를 선택하고 호출 순서를 정할 때 참고하는 지침입니다. 기존 시스템 메시지 뒤에 추가되며, 서브에이전트가 하나 이상 설정된 경우에만 사용합니다.',
                optional: true,
                acceptVariable: true,
                additionalParams: true
            },
            {
                label: '서브에이전트 설명 프롬프트',
                name: 'subAgentToolDescriptionPrompt',
                type: 'string',
                rows: 5,
                default:
                    '이 에이전트에 요청할 때는 전달 메시지만으로 작업을 이해할 수 있게 작성하세요. 앞 단계에서 확인한 실제 값과 대상 범위, 원하는 출력 형식을 포함하고, 목록을 참조할 때는 순번과 실제 항목명을 함께 적으세요.',
                description:
                    'Agent Card 설명 뒤에 덧붙여 마스터 모델에 보여 줄 안내문입니다. 어떤 요청을 어떤 형식으로 전달할지 정할 때 사용하며, 실제 서브에이전트에는 완성된 메시지만 보냅니다.',
                optional: true,
                acceptVariable: true,
                additionalParams: true
            },
            {
                // [GenOS #15904] 한 턴에 도구(MCP 포함)를 과도하게 연속 호출하는 것을 방지.
                // 2.2.3 Conversation Agent 의 Max Iteration 에 대응. 미설정/0 이면 무제한(기존 동작).
                label: 'Max Iterations',
                name: 'agentMaxIterations',
                type: 'number',
                description: 'Agent의 도구 호출 및 필수 스킬 결정 재시도 최대 라운드 수입니다. 한도까지 스킬 또는 폴백을 선언하지 못하면 자동 폴백으로 마무리합니다. 미설정 또는 0 이면 무제한.',
                optional: true,
                additionalParams: true
            },
            {
                label: '처리 단계 한도 안내 문구',
                name: 'agentIterationLimitMessage',
                type: 'string',
                rows: 3,
                default: DEFAULT_AGENT_ITERATION_LIMIT_MESSAGE,
                description: '처리 단계 한도에 도달하여 작업을 완료하지 못했을 때 표시합니다. 비워 두면 기본 안내 문구를 사용합니다.',
                optional: true,
                additionalParams: true
            },
            {
                label: 'Knowledge (Document Stores)',
                name: 'agentKnowledgeDocumentStores',
                type: 'array',
                description: 'Give your agent context about different document sources. Document stores must be upserted in advance.',
                client: ['agentflowv2'],
                array: [
                    {
                        label: 'Document Store',
                        name: 'documentStore',
                        type: 'asyncOptions',
                        loadMethod: 'listStores'
                    },
                    {
                        label: 'Describe Knowledge',
                        name: 'docStoreDescription',
                        type: 'string',
                        generateDocStoreDescription: true,
                        placeholder:
                            'Describe what the knowledge base is about, this is useful for the AI to know when and how to search for correct information',
                        rows: 4
                    },
                    {
                        label: 'Return Source Documents',
                        name: 'returnSourceDocuments',
                        type: 'boolean',
                        optional: true
                    }
                ],
                optional: true
            },
            {
                label: 'Knowledge (Vector Embeddings)',
                name: 'agentKnowledgeVSEmbeddings',
                type: 'array',
                description: 'Give your agent context about different document sources from existing vector stores and embeddings',
                client: ['agentflowv2'],
                array: [
                    {
                        label: 'Vector Store',
                        name: 'vectorStore',
                        type: 'asyncOptions',
                        loadMethod: 'listVectorStores',
                        loadConfig: true
                    },
                    {
                        label: 'Embedding Model',
                        name: 'embeddingModel',
                        type: 'asyncOptions',
                        loadMethod: 'listEmbeddings',
                        loadConfig: true
                    },
                    {
                        label: 'Knowledge Name',
                        name: 'knowledgeName',
                        type: 'string',
                        placeholder:
                            'A short name for the knowledge base, this is useful for the AI to know when and how to search for correct information'
                    },
                    {
                        label: 'Describe Knowledge',
                        name: 'knowledgeDescription',
                        type: 'string',
                        placeholder:
                            'Describe what the knowledge base is about, this is useful for the AI to know when and how to search for correct information',
                        rows: 4
                    },
                    {
                        label: 'Return Source Documents',
                        name: 'returnSourceDocuments',
                        type: 'boolean',
                        optional: true
                    }
                ],
                optional: true
            },
            {
                label: 'Enable Memory',
                name: 'agentEnableMemory',
                type: 'boolean',
                description: 'Enable memory for the conversation thread',
                default: true,
                optional: true
            },
            // [GenOS] 개인화 장기 메모리 자동 recall 주입 (에이전트 도구 호출과 별개, add-only)
            {
                label: '장기 메모리 자동 recall',
                name: 'enableLongTermRecall',
                type: 'boolean',
                description:
                    '켜면 이 Agent 노드 실행(Iteration은 항목별)의 첫 LLM 호출 전에 개인화 장기 메모리를 1회 검색해 주입한다(에이전트 도구 호출과 별개).',
                default: false,
                optional: true
            },
            {
                label: '개인화 메모리 MCP 서버',
                name: 'longTermMemoryMCPServerConfig',
                type: 'asyncOptions',
                loadMethod: 'getMemoryMCP',
                description: '개인화 메모리 MCP 서버 선택',
                show: {
                    enableLongTermRecall: true
                },
                additionalParams: true,
                optional: true
            },
            {
                label: '최대 검색 개수(k)',
                name: 'longTermRecallTopK',
                type: 'number',
                default: 8,
                show: {
                    enableLongTermRecall: true
                },
                additionalParams: true,
                optional: true
            },
            {
                label: '유사도 threshold(min_score)',
                name: 'longTermRecallThreshold',
                type: 'number',
                default: 0,
                description: '이 값 미만 유사도 기억 제외. 0=컷 없음. Weaviate hybrid score 스케일에 맞춰 조정.',
                show: {
                    enableLongTermRecall: true
                },
                additionalParams: true,
                optional: true
            },
            {
                label: '검색 범위',
                name: 'longTermRecallScope',
                type: 'multiOptions',
                options: [
                    { label: '개인(전 서비스 공통)', name: 'personal' },
                    { label: '현재 서비스', name: 'service' }
                ],
                default: ['personal'],
                description: '둘 다 선택하면 개인 메모리와 현재 서비스 메모리를 합쳐 검색합니다.',
                show: {
                    enableLongTermRecall: true
                },
                additionalParams: true,
                optional: true
            },
            {
                label: '검색 컨텍스트 주입 방식',
                name: 'longTermRecallInjectionMode',
                type: 'options',
                options: [
                    {
                        label: '사용자 컨텍스트 (권장)',
                        name: 'userContext',
                        description: '동적 메모리 데이터를 현재 사용자 질문 바로 앞에 낮은 권한의 참고 컨텍스트로 둔다.'
                    },
                    {
                        label: 'System 컨텍스트 (호환)',
                        name: 'system',
                        description: '애플리케이션 system 규칙 뒤에 메모리 컨텍스트를 병합한다.'
                    }
                ],
                default: 'userContext',
                show: {
                    enableLongTermRecall: true
                },
                additionalParams: true,
                optional: true
            },
            {
                label: '검색 컨텍스트 템플릿',
                name: 'longTermRecallContextTemplate',
                type: 'string',
                rows: 10,
                acceptVariable: true,
                default: DEFAULT_LONG_TERM_RECALL_CONTEXT_TEMPLATE,
                description:
                    '안전 안내·구분자 등 recall 프롬프트 전체 설정. {memories} 또는 {memories_json} 필수. 선택값: {query_time}, {count}, {safety}. {memories}는 번호가 붙은 메모리 JSON 목록이다.',
                show: {
                    enableLongTermRecall: true
                },
                additionalParams: true,
                optional: true
            },
            {
                label: 'Memory Type',
                name: 'agentMemoryType',
                type: 'options',
                options: [
                    {
                        label: 'All Messages',
                        name: 'allMessages',
                        description: 'Retrieve all messages from the conversation'
                    },
                    {
                        label: 'Window Size',
                        name: 'windowSize',
                        description: 'Uses a fixed window size to surface the last N messages'
                    },
                    {
                        label: 'Conversation Summary',
                        name: 'conversationSummary',
                        description: 'Summarizes the whole conversation'
                    },
                    {
                        label: 'Conversation Summary Buffer',
                        name: 'conversationSummaryBuffer',
                        description: 'Summarize conversations once token limit is reached. Default to 2000'
                    }
                ],
                optional: true,
                default: 'allMessages',
                show: {
                    agentEnableMemory: true
                }
            },
            {
                label: 'Window Size',
                name: 'agentMemoryWindowSize',
                type: 'number',
                default: '20',
                description: 'Uses a fixed window size to surface the last N messages',
                show: {
                    agentMemoryType: 'windowSize'
                }
            },
            {
                label: 'Max Token Limit',
                name: 'agentMemoryMaxTokenLimit',
                type: 'number',
                default: '2000',
                description: 'Summarize conversations once token limit is reached. Default to 2000',
                show: {
                    agentMemoryType: 'conversationSummaryBuffer'
                }
            },
            {
                label: 'Input Message',
                name: 'agentUserMessage',
                type: 'string',
                description: 'Add an input message as user message at the end of the conversation',
                rows: 4,
                optional: true,
                acceptVariable: true,
                show: {
                    agentEnableMemory: true
                }
            },
            {
                label: 'Return Response As',
                name: 'agentReturnResponseAs',
                type: 'options',
                options: [
                    {
                        label: 'User Message',
                        name: 'userMessage'
                    },
                    {
                        label: 'Assistant Message',
                        name: 'assistantMessage'
                    }
                ],
                default: 'userMessage'
            },
            {
                label: 'JSON Structured Output',
                name: 'agentStructuredOutput',
                description: 'Instruct the Agent to give output in a JSON structured schema',
                type: 'array',
                optional: true,
                acceptVariable: true,
                array: [
                    {
                        label: 'Key',
                        name: 'key',
                        type: 'string'
                    },
                    {
                        label: 'Type',
                        name: 'type',
                        type: 'options',
                        options: [
                            {
                                label: 'String',
                                name: 'string'
                            },
                            {
                                label: 'String Array',
                                name: 'stringArray'
                            },
                            {
                                label: 'Number',
                                name: 'number'
                            },
                            {
                                label: 'Boolean',
                                name: 'boolean'
                            },
                            {
                                label: 'Enum',
                                name: 'enum'
                            },
                            {
                                label: 'JSON Array',
                                name: 'jsonArray'
                            }
                        ]
                    },
                    {
                        label: 'Enum Values',
                        name: 'enumValues',
                        type: 'string',
                        placeholder: 'value1, value2, value3',
                        description: 'Enum values. Separated by comma',
                        optional: true,
                        show: {
                            'agentStructuredOutput[$index].type': 'enum'
                        }
                    },
                    {
                        label: 'JSON Schema',
                        name: 'jsonSchema',
                        type: 'code',
                        placeholder: `{
    "answer": {
        "type": "string",
        "description": "Value of the answer"
    },
    "reason": {
        "type": "string",
        "description": "Reason for the answer"
    },
    "optional": {
        "type": "boolean"
    },
    "count": {
        "type": "number"
    },
    "children": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "string",
                    "description": "Value of the children's answer"
                }
            }
        }
    }
}`,
                        description: 'JSON schema for the structured output',
                        optional: true,
                        hideCodeExecute: true,
                        show: {
                            'agentStructuredOutput[$index].type': 'jsonArray'
                        }
                    },
                    {
                        label: 'Description',
                        name: 'description',
                        type: 'string',
                        placeholder: 'Description of the key'
                    }
                ]
            },
            {
                label: 'Update Flow State',
                name: 'agentUpdateState',
                description: 'Update runtime state during the execution of the workflow',
                type: 'array',
                optional: true,
                acceptVariable: true,
                array: [
                    {
                        label: 'Key',
                        name: 'key',
                        type: 'asyncOptions',
                        loadMethod: 'listRuntimeStateKeys'
                    },
                    {
                        label: 'Value',
                        name: 'value',
                        type: 'string',
                        acceptVariable: true,
                        acceptNodeOutputAsVariable: true
                    }
                ]
            }
        ]
```

## Retriever

경로: `flowise/3.0.0/before_install/packages/components/nodes/agentflow/Retriever/Retriever.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/agentflow/Retriever/Retriever.ts)

```typescript
[
            {
                label: 'Knowledge (Document Stores)',
                name: 'retrieverKnowledgeDocumentStores',
                type: 'array',
                description: 'Document stores to retrieve information from. Document stores must be upserted in advance.',
                array: [
                    {
                        label: 'Document Store',
                        name: 'documentStore',
                        type: 'asyncOptions',
                        loadMethod: 'listStores'
                    }
                ]
            },
            {
                label: 'Retriever Query',
                name: 'retrieverQuery',
                type: 'string',
                placeholder: 'Enter your query here',
                rows: 4,
                acceptVariable: true
            },
            {
                label: 'Output Format',
                name: 'outputFormat',
                type: 'options',
                options: [
                    { label: 'Text', name: 'text' },
                    { label: 'Text with Metadata', name: 'textWithMetadata' }
                ],
                default: 'text'
            },
            {
                label: 'Is Ground Truth',
                name: 'isGroundTruth',
                type: 'boolean',
                default: false,
                optional: true,
                description: 'When enabled, the retrieved content is stored in trace metadata as ground_truth for evaluation. Not passed to the Agent.'
            },
            {
                label: 'Ground Truth Retriever',
                name: 'groundTruthRetriever',
                type: 'BaseRetriever',
                optional: true,
                description: 'VectorStore retriever for ground truth Q&A dataset. Required when Is Ground Truth is enabled and knowledge is stored as a Vector Embeddings (AI Drive). The retrieved [ANSWER] is stored in trace metadata — not passed to the Agent.'
            },
            {
                label: 'Update Flow State',
                name: 'retrieverUpdateState',
                description: 'Update runtime state during the execution of the workflow',
                type: 'array',
                optional: true,
                acceptVariable: true,
                array: [
                    {
                        label: 'Key',
                        name: 'key',
                        type: 'asyncOptions',
                        loadMethod: 'listRuntimeStateKeys',
                        freeSolo: true
                    },
                    {
                        label: 'Value',
                        name: 'value',
                        type: 'string',
                        acceptVariable: true,
                        acceptNodeOutputAsVariable: true
                    }
                ]
            }
        ]
```

## Tool

경로: `flowise/3.0.0/before_install/packages/components/nodes/agentflow/Tool/Tool.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/agentflow/Tool/Tool.ts)

```typescript
[
            {
                label: 'Tool',
                name: 'toolAgentflowSelectedTool',
                type: 'asyncOptions',
                loadMethod: 'listTools',
                loadConfig: true
            },
            {
                label: 'Tool Input Arguments',
                name: 'toolInputArgs',
                type: 'array',
                acceptVariable: true,
                refresh: true,
                array: [
                    {
                        label: 'Input Argument Name',
                        name: 'inputArgName',
                        type: 'asyncOptions',
                        loadMethod: 'listToolInputArgs',
                        refresh: true
                    },
                    {
                        label: 'Input Argument Value',
                        name: 'inputArgValue',
                        type: 'string',
                        acceptVariable: true
                    }
                ],
                show: {
                    toolAgentflowSelectedTool: '.+'
                }
            },
            {
                // [GenOS] 규칙 기반 절차에서는 어떤 도구를 부를지 실행 중에 정해진다.
                // asyncOptions 는 설계 시점에 고르는 것이라 상태 주입용 문자열 입력을 따로 둔다.
                label: '도구 이름 (상태 값)',
                name: 'toolFromState',
                type: 'string',
                optional: true,
                acceptVariable: true,
                placeholder: '{{ $flow.state.step_tool }}',
                description: '지정하면 위에서 고른 도구 대신 이 값을 쓴다.'
            },
            {
                // 배열 입력에 문자열을 넣으면 편집 화면이 깨지므로(ArrayRenderer) 문자열 전용 입력을 둔다.
                label: '도구 인자 (상태 값, JSON)',
                name: 'toolInputArgsJson',
                type: 'string',
                optional: true,
                acceptVariable: true,
                placeholder: '{{ $flow.state.step_args }}',
                description: 'JSON 객체 문자열. 지정하면 위의 인자 목록 대신 이 값을 쓴다.'
            },
            {
                label: 'Update Flow State',
                name: 'toolUpdateState',
                description: 'Update runtime state during the execution of the workflow',
                type: 'array',
                optional: true,
                acceptVariable: true,
                array: [
                    {
                        label: 'Key',
                        name: 'key',
                        type: 'asyncOptions',
                        loadMethod: 'listRuntimeStateKeys',
                        freeSolo: true
                    },
                    {
                        label: 'Value',
                        name: 'value',
                        type: 'string',
                        acceptVariable: true,
                        acceptNodeOutputAsVariable: true
                    }
                ]
            }
        ]
```

## MncUnifiedRagChain

경로: `flowise/3.0.0/before_install/packages/components/nodes/chains/MncUnifiedRagChain/MncUnifiedRagChain.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/chains/MncUnifiedRagChain/MncUnifiedRagChain.ts)

```typescript
[
            {
                label: 'Chat Model',
                name: 'model',
                type: 'BaseChatModel'
            },
            {
                label: 'Vector Store Retriever',
                name: 'vectorStoreRetriever',
                type: 'BaseRetriever'
            },
            {
                label: 'Max Context Character',
                description: 'Max Context Character Limit',
                name: 'maxContextToken',
                type: 'number',
                default: 7000
            },
            {
                label: 'Add Meta Info',
                name: 'addMetaInfo',
                type: 'string',
                description: '검색된 결과에서 포함된 메타 정보까지 LLM에 전달합니다.',
                warning: '입력한 메타 정보가 벡터DB에 포함되있어야합니다.',
                optional: true,
                additionalParams: true,
                default: `['file_name']`
            },
            {
                label: 'Rephrase Prompt',
                name: 'rephrasePrompt',
                type: 'string',
                description: '이전 대화 기록을 사용하여 질문을 재구성합니다. memory 연결시 활성화됩니다.',
                warning: 'Prompt must include input variables: {chat_history} and {question}',
                rows: 4,
                additionalParams: true,
                optional: true,
                default: REPHRASE_TEMPLATE
            },            
            {
                label: 'Prompt',
                name: 'prompt',
                type: 'BasePromptTemplate',
                description: 'Prompt for the RAG chain',
                warning: 'Prompt must include input variables: {context} and {question}',
                optional: true,
                default: RESPONSE_TEMPLATE
            },
            {
                label: 'Memory',
                name: 'memory',
                type: 'BaseMemory',
                optional: true,
                description: '연결시 멀티턴 대화 모드로 작동합니다.'
            },
            {
                label: 'FAQ Retriever',
                name: 'faqStoreRetriever',
                type: 'BaseRetriever',
                optional: true,
                description: 'FAQ retriever for verified QA'
            },
            {
                label: 'Ground Truth Retriever',
                name: 'groundTruthRetriever',
                type: 'BaseRetriever',
                optional: true,
                description: 'Retriever for evaluation ground truth. The retrieved answer is stored in trace metadata as ground_truth — not passed to the LLM.'
            },
            {
                label: 'FAQ Answer Key',
                name: 'faqAnswerKey',
                type: 'string',
                default: 'pageContent',
                optional: true,
                description: 'Required if FAQ Retriever is connected'
            },
            {
                label: 'Return Source Documents',
                name: 'returnSourceDocuments',
                type: 'boolean',
                optional: true,
                default: true
            },
            {
                label: 'Input Moderation',
                description: 'Detect text that could generate harmful output and prevent it from being sent to the language model',
                name: 'inputModeration',
                type: 'Moderation',
                optional: true,
                list: true
            }
        ]
```

## ChatMnc

경로: `flowise/3.0.0/before_install/packages/components/nodes/chatmodels/ChatMnc/ChatMnc.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/chatmodels/ChatMnc/ChatMnc.ts)

```typescript
[
            {
                label: 'Cache',
                name: 'cache',
                type: 'BaseCache',
                optional: true
            },
            {
                // P6: 직접 연결 / 서비스 라우터 연결 분기. 'service-router' 선택 시 아래 'Service Router'
                // 셀렉터를 채우면 되고, 'serving' (default) 은 기존처럼 Serving/Revision 셀렉터를 사용.
                label: 'Connection Type',
                name: 'connectionType',
                type: 'options',
                options: [
                    { label: 'Direct Serving', name: 'serving' },
                    { label: 'Service Router', name: 'service-router' }
                ],
                default: 'serving'
            },
            {
                label: 'Serving',
                name: 'serving',
                type: 'asyncOptions',
                loadMethod: 'getServingList',
                optional: true,
                show: { connectionType: 'serving' }
            },
            {
                label: 'Serving Revision',
                name: 'servingRevision',
                description: '미설정시 대표 리비전을 사용합니다.',
                type: 'asyncOptions',
                loadMethod: 'getServingRevisionList',
                optional: true,
                show: { connectionType: 'serving' }
            },
            {
                label: 'Service Router',
                name: 'serviceRouter',
                description: 'Connection Type 이 Service Router 일 때 사용. /service-router/{endpoint} 로 외부 호출.',
                type: 'asyncOptions',
                loadMethod: 'getServiceRouterList',
                optional: true,
                show: { connectionType: 'service-router' }
            },
            {
                label: 'Max Tokens',
                name: 'maxTokens',
                type: 'number',
                step: 1,
                default: 512
            },
            {
                label: 'Temperature',
                name: 'temperature',
                type: 'number',
                step: 0.1,
                default: 0.9,
                optional: true
            },
            {
                label: 'Streaming',
                name: 'streaming',
                type: 'boolean',
                default: true,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Top Probability',
                name: 'topP',
                type: 'number',
                step: 0.1,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Frequency Penalty',
                name: 'frequencyPenalty',
                type: 'number',
                step: 0.1,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Presence Penalty',
                name: 'presencePenalty',
                type: 'number',
                step: 0.1,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Top K',
                name: 'topK',
                type: 'number',
                step: 1,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Min P',
                name: 'minP',
                type: 'number',
                step: 0.01,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Repetition Penalty',
                name: 'repetitionPenalty',
                type: 'number',
                step: 0.01,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Timeout',
                name: 'timeout',
                type: 'number',
                step: 1,
                optional: true,
                additionalParams: true
            },
            {
                label: 'BaseOptions',
                name: 'baseOptions',
                type: 'json',
                optional: true,
                additionalParams: true
            },
            {
                label: 'Allow Image Uploads',
                name: 'allowImageUploads',
                type: 'boolean',
                description:
                    'Automatically uses gpt-4-vision-preview when image is being uploaded from chat. Only works with LLMChain, Conversation Chain, ReAct Agent, and Conversational Agent',
                default: false,
                optional: true
            },
            {
                label: 'Image Resolution',
                description: 'This parameter controls the resolution in which the model views the image.',
                name: 'imageResolution',
                type: 'options',
                options: [
                    {
                        label: 'Low',
                        name: 'low'
                    },
                    {
                        label: 'High',
                        name: 'high'
                    },
                    {
                        label: 'Auto',
                        name: 'auto'
                    }
                ],
                default: 'low',
                optional: false,
                additionalParams: true
            }            
        ]
```

## ChatOpenAI

경로: `flowise/3.0.0/before_install/packages/components/nodes/chatmodels/ChatOpenAI/ChatOpenAI.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/chatmodels/ChatOpenAI/ChatOpenAI.ts)

```typescript
[
            {
                label: 'Cache',
                name: 'cache',
                type: 'BaseCache',
                optional: true
            },
            {
                label: 'Model Name',
                name: 'modelName',
                type: 'asyncOptions',
                loadMethod: 'listModels',
                default: 'gpt-4o-mini'
            },
            {
                label: 'Temperature',
                name: 'temperature',
                type: 'number',
                step: 0.1,
                default: 0.9,
                optional: true
            },
            {
                label: 'Streaming',
                name: 'streaming',
                type: 'boolean',
                default: true,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Allow Image Uploads',
                name: 'allowImageUploads',
                type: 'boolean',
                description:
                    'Allow image input. Refer to the <a href="https://docs.flowiseai.com/using-flowise/uploads#image" target="_blank">docs</a> for more details.',
                default: false,
                optional: true
            },
            {
                label: 'Reasoning',
                description: 'Whether the model supports reasoning. Only applicable for reasoning models (gpt-5 and o-series models only)',
                name: 'reasoning',
                type: 'boolean',
                default: false,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Reasoning Effort',
                description: 'Constrains effort on reasoning. Only applicable for reasoning models (gpt-5 and o-series models only)',
                name: 'reasoningEffort',
                type: 'options',
                options: [
                    {
                        label: 'Low',
                        name: 'low'
                    },
                    {
                        label: 'Medium',
                        name: 'medium'
                    },
                    {
                        label: 'High',
                        name: 'high'
                    },
                    {
                        label: 'X-High',
                        name: 'xhigh',
                        description: 'X-High is supported for all models after gpt-5.1-codex-max'
                    }
                ],
                additionalParams: true,
                show: {
                    reasoning: true
                }
            },
            {
                label: 'Reasoning Summary',
                description: `A summary of the reasoning performed by the model. This can be useful for debugging and understanding the model's reasoning process`,
                name: 'reasoningSummary',
                type: 'options',
                options: [
                    {
                        label: 'Auto',
                        name: 'auto'
                    },
                    {
                        label: 'Concise',
                        name: 'concise'
                    },
                    {
                        label: 'Detailed',
                        name: 'detailed'
                    }
                ],
                additionalParams: true,
                show: {
                    reasoning: true
                }
            },
            {
                label: 'Max Tokens',
                name: 'maxTokens',
                type: 'number',
                step: 1,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Top Probability',
                name: 'topP',
                type: 'number',
                step: 0.1,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Frequency Penalty',
                name: 'frequencyPenalty',
                type: 'number',
                step: 0.1,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Presence Penalty',
                name: 'presencePenalty',
                type: 'number',
                step: 0.1,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Timeout',
                name: 'timeout',
                type: 'number',
                step: 1,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Strict Tool Calling',
                name: 'strictToolCalling',
                type: 'boolean',
                description:
                    'Whether the model supports the `strict` argument when passing in tools. If not specified, the `strict` argument will not be passed to OpenAI.',
                optional: true,
                additionalParams: true
            },
            {
                label: 'Stop Sequence',
                name: 'stopSequence',
                type: 'string',
                rows: 4,
                optional: true,
                description: 'List of stop words to use when generating. Use comma to separate multiple stop words.',
                additionalParams: true
            },
            {
                label: 'Base Path',
                name: 'basepath',
                type: 'string',
                optional: true,
                description: 'Override the default base URL for the API, e.g., "https://api.example.com/v2/',
                additionalParams: true
            },
            {
                label: 'Base Options',
                name: 'baseOptions',
                type: 'json',
                optional: true,
                description: 'Default headers to include with every request to the API.',
                additionalParams: true
            }
        ]
```

## ChatOpenAICustom

경로: `flowise/3.0.0/before_install/packages/components/nodes/chatmodels/ChatOpenAICustom/ChatOpenAICustom.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/chatmodels/ChatOpenAICustom/ChatOpenAICustom.ts)

```typescript
[
            {
                label: 'Cache',
                name: 'cache',
                type: 'BaseCache',
                optional: true
            },
            {
                label: 'Model Name',
                name: 'modelName',
                type: 'string',
                placeholder: 'ft:gpt-3.5-turbo:my-org:custom_suffix:id'
            },
            {
                label: 'Temperature',
                name: 'temperature',
                type: 'number',
                step: 0.1,
                default: 0.9,
                optional: true
            },
            {
                label: 'Streaming',
                name: 'streaming',
                type: 'boolean',
                default: true,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Max Tokens',
                name: 'maxTokens',
                type: 'number',
                step: 1,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Top Probability',
                name: 'topP',
                type: 'number',
                step: 0.1,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Frequency Penalty',
                name: 'frequencyPenalty',
                type: 'number',
                step: 0.1,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Presence Penalty',
                name: 'presencePenalty',
                type: 'number',
                step: 0.1,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Timeout',
                name: 'timeout',
                type: 'number',
                step: 1,
                optional: true,
                additionalParams: true
            },
            {
                label: 'BasePath',
                name: 'basepath',
                type: 'string',
                optional: true,
                additionalParams: true
            },
            {
                label: 'BaseOptions',
                name: 'baseOptions',
                type: 'json',
                optional: true,
                additionalParams: true
            },
            {
                label: 'Allow Image Uploads',
                name: 'allowImageUploads',
                type: 'boolean',
                description:
                    'Automatically uses gpt-4-vision-preview when image is being uploaded from chat. Only works with LLMChain, Conversation Chain, ReAct Agent, and Conversational Agent',
                default: false,
                optional: true
            },
            {
                label: 'Image Resolution',
                description: 'This parameter controls the resolution in which the model views the image.',
                name: 'imageResolution',
                type: 'options',
                options: [
                    {
                        label: 'Low',
                        name: 'low'
                    },
                    {
                        label: 'High',
                        name: 'high'
                    },
                    {
                        label: 'Auto',
                        name: 'auto'
                    }
                ],
                default: 'low',
                optional: false,
                additionalParams: true
            }                    
        ]
```

## MncOpenAIEmbedding

경로: `flowise/3.0.0/before_install/packages/components/nodes/embeddings/MncOpenAIEmbedding/MncOpenAIEmbedding.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/embeddings/MncOpenAIEmbedding/MncOpenAIEmbedding.ts)

```typescript
[
            {
                // 직접 연결 / 서비스 라우터 연결 분기. 'service-router' 선택 시 아래 'Service Router'
                // 셀렉터를 채우면 되고, 'serving' (default) 은 기존처럼 Serving/Revision 셀렉터를 사용.
                label: 'Connection Type',
                name: 'connectionType',
                type: 'options',
                options: [
                    { label: 'Direct Serving', name: 'serving' },
                    { label: 'Service Router', name: 'service-router' }
                ],
                default: 'serving'
            },
            {
                label: 'Serving',
                name: 'serving',
                type: 'asyncOptions',
                loadMethod: 'getServingList',
                optional: true,
                show: { connectionType: 'serving' }
            },
            {
                label: 'Serving Revision',
                name: 'servingRevision',
                description: '미설정시 대표 리비전을 사용합니다.',
                type: 'asyncOptions',
                loadMethod: 'getServingRevisionList',
                optional: true,
                show: { connectionType: 'serving' }
            },
            {
                label: 'Service Router',
                name: 'serviceRouter',
                description: 'Connection Type 이 Service Router 일 때 사용. /service-router/{endpoint} 로 외부 호출.',
                type: 'asyncOptions',
                loadMethod: 'getServiceRouterList',
                optional: true,
                show: { connectionType: 'service-router' }
            },
            {
                label: 'Strip New Lines',
                name: 'stripNewLines',
                type: 'boolean',
                optional: true,
                additionalParams: true
            },
            {
                label: 'Batch Size',
                name: 'batchSize',
                type: 'number',
                optional: true,
                additionalParams: true
            },
            {
                label: 'Timeout',
                name: 'timeout',
                type: 'number',
                optional: true,
                additionalParams: true
            },
            {
                label: 'Dimensions',
                name: 'dimensions',
                type: 'number',
                optional: true,
                additionalParams: true
            },
            {
                label: 'BaseOptions',
                name: 'baseOptions',
                type: 'json',
                optional: true,
                additionalParams: true
            },            
        ]
```

## MncLLMFilterCompressionRetriever

경로: `flowise/3.0.0/before_install/packages/components/nodes/retrievers/MncLLMFilterRetriever/MncLLMFilterCompressionRetriever.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/retrievers/MncLLMFilterRetriever/MncLLMFilterCompressionRetriever.ts)

```typescript
[
            {
                label: 'Vector Store Retriever',
                name: 'baseRetriever',
                type: 'VectorStoreRetriever'
            },
            {
                label: 'Language Model',
                name: 'model',
                type: 'BaseLanguageModel'
            },
            {
                label: 'Query',
                name: 'query',
                type: 'string',
                description: '문서를 검색하기 위한 검색어입니다. 지정되지 않은 경우, 사용자 질문이 사용됩니다.',
                optional: true,
                acceptVariable: true
            },
            {
                label: 'Filter Prompt',
                name: 'filterPrompt',
                type: 'string',
                description: '질문에 연관된 문서를 필터링하는 프롬프트',
                warning: 'Prompt must include input variable:{question} and {context}',
                rows: 4,
                additionalParams: true,
                optional: true,
                default: FILTER_TEMPLATE // FILTER_TEMPLATE 으로 바꾸고 싶음.
            }
        ]
```

## MncMergeRetriever

경로: `flowise/3.0.0/before_install/packages/components/nodes/retrievers/MncMergeRetriever/MncMergeRetriever.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/retrievers/MncMergeRetriever/MncMergeRetriever.ts)

```typescript
[
            {
                label: 'Vector Store Retrievers',
                name: 'baseRetrievers',
                type: 'BaseRetriever',
                list: true // Indicate that this input can accept multiple retrievers
            },
            {
                label: 'Embeddings',
                name: 'embeddings',
                type: 'Embeddings'
            },
            {
                label: 'Query',
                name: 'query',
                type: 'string',
                description: 'Query to retrieve documents from retriever. If not specified, user question will be used',
                optional: true,
                acceptVariable: true
            },
            {
                label: 'Similarity Threshold',
                name: 'similarityThreshold',
                description:
                    'Threshold for determining when two documents are similar enough to be considered redundant. Must be specified if `k` is not set',
                type: 'number',
                default: 0.8,
                step: 0.1,
                optional: true
            },
            {
                label: 'K',
                name: 'k',
                description:
                    'The number of relevant documents to return. Can be explicitly set to undefined, in which case similarity_threshold must be specified. Defaults to 20',
                type: 'number',
                default: 20,
                step: 1,
                optional: true,
                additionalParams: true
            }
        ]
```

## MncRerankRetriever

경로: `flowise/3.0.0/before_install/packages/components/nodes/retrievers/MncRerankRetriever/MncRerankRetriever.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/retrievers/MncRerankRetriever/MncRerankRetriever.ts)

```typescript
[
            {
                label: 'Vector Store Retrievers',
                name: 'baseRetrievers',
                type: 'BaseRetriever',
                list: true,
                description: '여러 리트리버를 입력하면 병합 후 리랭킹합니다. 단일 리트리버도 지원합니다.'
            },
            {
                // 직접 연결 / 서비스 라우터 연결 분기. 'service-router' 선택 시 아래 'Service Router'
                // 셀렉터를 채우면 되고, 'serving' (default) 은 기존처럼 Serving 셀렉터를 사용.
                label: 'Connection Type',
                name: 'connectionType',
                type: 'options',
                options: [
                    { label: 'Direct Serving', name: 'serving' },
                    { label: 'Service Router', name: 'service-router' }
                ],
                default: 'serving'
            },
            {
                label: 'Serving',
                name: 'serving',
                type: 'asyncOptions',
                loadMethod: 'getRerankList',
                optional: true,
                show: { connectionType: 'serving' }
            },
            {
                label: 'Service Router',
                name: 'serviceRouter',
                description: 'Connection Type 이 Service Router 일 때 사용. /service-router/{endpoint} 로 외부 호출.',
                type: 'asyncOptions',
                loadMethod: 'getServiceRouterList',
                optional: true,
                show: { connectionType: 'service-router' }
            },
            {
                label: 'Embeddings',
                name: 'embeddings',
                type: 'Embeddings',
                optional: true,
                description: '임베딩 필터를 사용할 경우 필요합니다. 사용하지 않을 경우 생략 가능합니다.'
            },
            {
                label: 'Query',
                name: 'query',
                type: 'string',
                description: 'Query to retrieve documents from retriever. If not specified, user question will be used',
                optional: true,
                acceptVariable: true
            },
            {
                label: 'Top K',
                name: 'topK',
                description: 'Number of top results to fetch. Default to the TopK of the Base Retriever',
                placeholder: '4',
                type: 'number',
                additionalParams: true,
                optional: true
            },
            {
                label: 'Use Embeddings Filter',
                name: 'useEmbeddingsFilter',
                type: 'boolean',
                default: false,
                optional: true,
                additionalParams: true,
                description: '임베딩 필터를 사용하여 관련성이 낮은 문서를 제거합니다.'
            },
            {
                label: 'Similarity Threshold',
                name: 'similarityThreshold',
                description: '임베딩 필터 사용 시 유사도 임계값입니다. 이 값보다 낮은 유사도를 가진 문서는 제거됩니다.',
                type: 'number',
                default: 0.8,
                step: 0.1,
                optional: true,
                additionalParams: true
            }
        ]
```

## GenOSLongTermMemory

경로: `flowise/3.0.0/before_install/packages/components/nodes/tools/GenOSMemory/GenOSLongTermMemory.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/tools/GenOSMemory/GenOSLongTermMemory.ts)

```typescript
[
            {
                label: '메모리 MCP 서버',
                name: 'memoryMCPServerConfig',
                type: 'asyncOptions',
                loadMethod: 'getMemoryMCP',
                description: '개인화 메모리 MCP 서버(code-serving)를 선택하세요.'
            },
            {
                label: '사용할 기억 도구',
                name: 'mcpActions',
                type: 'asyncMultiOptions',
                loadMethod: 'listActions',
                refresh: true,
                description: 'recall(조회)·detail(상세)·save(저장) 중 노출할 도구'
            },
            {
                label: '검색 범위',
                name: 'longTermRecallScope',
                type: 'multiOptions',
                options: [
                    { label: '개인(전 서비스 공통)', name: 'personal' },
                    { label: '현재 서비스', name: 'service' }
                ],
                default: ['personal'],
                description: 'recall에 적용. 둘 다 선택하면 개인 메모리와 현재 서비스 메모리를 합쳐 검색합니다.',
                optional: true
            },
            {
                label: '타임아웃(초)',
                name: 'timeout',
                type: 'number',
                description: 'MCP 서버 호출 타임아웃(초). 미설정 시 기본 180초.',
                default: 180,
                additionalParams: true,
                optional: true
            }
        ]
```

## GenosMCP

경로: `flowise/3.0.0/before_install/packages/components/nodes/tools/MCP/GenosMCP/GenosMCP.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/tools/MCP/GenosMCP/GenosMCP.ts)

```typescript
[
            {
                label: 'Genos MCP Server',
                name: 'genosMCPServerConfig',
                type: 'asyncOptions',
                loadMethod: 'getGenosMCP'
            },
            {
                label: '사용가능한 도구',
                name: 'mcpActions',
                type: 'asyncMultiOptions',
                loadMethod: 'listActions',
                refresh: true,
                // [GenOS] 비워 두면 이 서버의 **모든 도구**를 쓴다. 도구가 수십 개인 서버를
                // 하나씩 고르지 않아도 되고, 서버에 도구가 추가되면 자동으로 따라온다.
                // (장기기억 노드 GenOSLongTermMemory 가 이미 같은 규약을 쓴다 — 그것과 맞춘다.)
                optional: true,
                description: '비워 두면 이 서버의 모든 도구를 사용합니다. 일부만 쓰려면 골라 주세요.'
            },
            {
                label: '타임아웃(초)',
                name: 'timeout',
                type: 'number',
                description: 'MCP 서버 호출 요청 타임아웃(초). 미설정 시 기본 180초가 적용됩니다.',
                default: 180,
                additionalParams: true,
                optional: true
            }
        ]
```

## RetrieverTool

경로: `flowise/3.0.0/before_install/packages/components/nodes/tools/RetrieverTool/RetrieverTool.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/tools/RetrieverTool/RetrieverTool.ts)

```typescript
[
            {
                label: 'Retriever Name',
                name: 'name',
                type: 'string',
                placeholder: 'search_state_of_union'
            },
            {
                label: 'Retriever Description',
                name: 'description',
                type: 'string',
                description: 'When should agent uses to retrieve documents',
                rows: 3,
                placeholder: 'Searches and returns documents regarding the state-of-the-union.'
            },
            {
                label: 'Retriever',
                name: 'retriever',
                type: 'BaseRetriever'
            },
            {
                label: 'Return Source Documents',
                name: 'returnSourceDocuments',
                type: 'boolean',
                optional: true
            },
            {
                label: 'Additional Metadata Filter',
                name: 'retrieverToolMetadataFilter',
                type: 'json',
                description: 'Add additional metadata filter on top of the existing filter from vector store',
                optional: true,
                additionalParams: true,
                hint: {
                    label: 'What can you filter?',
                    value: howToUse
                }
            }
        ]
```

## DeepSearfing

경로: `flowise/3.0.0/before_install/packages/components/nodes/vectorstores/DeepSearfing/DeepSearfing.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/vectorstores/DeepSearfing/DeepSearfing.ts)

```typescript
[
            {
                label: 'Document',
                name: 'document',
                type: 'Document',
                list: true,
                optional: true
            },
            {
                label: 'Embeddings',
                name: 'embeddings',
                type: 'Embeddings'
            },
            {
                label: 'Record Manager',
                name: 'recordManager',
                type: 'RecordManager',
                description: 'Keep track of the record to prevent duplication',
                optional: true
            },
            // {
            //     label: 'Weaviate Scheme',
            //     name: 'weaviateScheme',
            //     type: 'options',
            //     default: 'https',
            //     options: [
            //         {
            //             label: 'https',
            //             name: 'https'
            //         },
            //         {
            //             label: 'http',
            //             name: 'http'
            //         }
            //     ]
            // },
            // Genos 도입시 필요 없는 항목이지만 그대로 놔둠.
            {
                label: 'Weaviate Host',
                name: 'weaviateHost',
                type: 'asyncOptions',
                loadMethod: 'listVectorDBs'
            },
            {
                label: 'Weaviate Index',
                name: 'weaviateIndex',
                type: 'asyncOptions',
                loadMethod: 'listIndices'
                // type: 'string',
                // placeholder: 'Test'
            },
            {
                label: 'Weaviate Text Key',
                name: 'weaviateTextKey',
                type: 'string',
                placeholder: 'text',
                optional: true,
                additionalParams: true
            },
            {
                label: 'Weaviate Metadata Keys',
                name: 'weaviateMetadataKeys',
                type: 'string',
                rows: 4,
                placeholder: `["foo"]`,
                default: `["i_page", "file_name", "file_path"]`,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Top K',
                name: 'topK',
                description: 'Number of top results to fetch. Default to 4',
                placeholder: '4',
                type: 'number',
                additionalParams: true,
                optional: true
            },
            {
                label: 'Weaviate Search Filter',
                name: 'weaviateFilter',
                type: 'json',
                additionalParams: true,
                optional: true
            }
        ]
```

## SkillPipeline

경로: `flowise/3.0.0/before_install/packages/components/nodes/vectorstores/DeepSearfing/SkillPipeline.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/vectorstores/DeepSearfing/SkillPipeline.ts)

```typescript
[
            {
                label: '스킬',
                name: 'skillDrive',
                type: 'asyncOptions',
                loadMethod: 'listSkillDrives',
                description: '관리자 페이지 「도구 > 스킬」 에 만든 드라이브'
            },
            {
                label: 'Embeddings',
                name: 'embeddings',
                type: 'Embeddings',
                optional: true
            },
            {
                label: 'Top K',
                name: 'topK',
                type: 'number',
                placeholder: '4',
                optional: true,
                additionalParams: true
            }
        ]
```

## Weaviate

경로: `flowise/3.0.0/before_install/packages/components/nodes/vectorstores/Weaviate/Weaviate.ts` · [기준 소스](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/vectorstores/Weaviate/Weaviate.ts)

```typescript
[
            {
                label: 'Document',
                name: 'document',
                type: 'Document',
                list: true,
                optional: true
            },
            {
                label: 'Embeddings',
                name: 'embeddings',
                type: 'Embeddings'
            },
            {
                label: 'Record Manager',
                name: 'recordManager',
                type: 'RecordManager',
                description: 'Keep track of the record to prevent duplication',
                optional: true
            },
            {
                label: 'Weaviate Scheme',
                name: 'weaviateScheme',
                type: 'options',
                default: 'https',
                options: [
                    {
                        label: 'https',
                        name: 'https'
                    },
                    {
                        label: 'http',
                        name: 'http'
                    }
                ]
            },
            {
                label: 'Weaviate Host',
                name: 'weaviateHost',
                type: 'string',
                placeholder: 'localhost:8080'
            },
            {
                label: 'Weaviate Index',
                name: 'weaviateIndex',
                type: 'string',
                placeholder: 'Test'
            },
            {
                label: 'Weaviate Text Key',
                name: 'weaviateTextKey',
                type: 'string',
                placeholder: 'text',
                optional: true,
                additionalParams: true
            },
            {
                label: 'Weaviate Metadata Keys',
                name: 'weaviateMetadataKeys',
                type: 'string',
                rows: 4,
                placeholder: `["foo"]`,
                optional: true,
                additionalParams: true
            },
            {
                label: 'Top K',
                name: 'topK',
                description: 'Number of top results to fetch. Default to 4',
                placeholder: '4',
                type: 'number',
                additionalParams: true,
                optional: true
            },
            {
                label: 'Weaviate Search Filter',
                name: 'weaviateFilter',
                type: 'json',
                additionalParams: true,
                optional: true
            }
        ]
```
