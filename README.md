
# AiRes: AI-Powered Research Paper Enhancement Tool

AiRes is an AI-powered tool that enhances research papers using Generative AI. It rewrites content in an academic style, converts bullet points into cohesive paragraphs, summarizes text for presentation slides, proofreads for grammar and clarity, and helps users find top-cited research papers.

### API Reference

#### **Generate Response using Cohere API**  
**POST** `/api/cohere/generate`  
**Parameters:**

| Parameter    | Type   | Description                                                                 |
|--------------|--------|-----------------------------------------------------------------------------|
| api_key      | string | Required. Your API key for accessing the Cohere API.                        |
| prompt       | string | Required. The text prompt for generating a response. This should include the task you want Cohere to perform. |
| max_tokens   | int    | Optional. The maximum number of tokens in the generated response (default: 200). |
| temperature  | float  | Optional. Controls the randomness of the response (default: 0.5). A lower temperature results in more focused, deterministic output. |

#### **Search Papers on CrossRef**  
**GET** `/api/crossref/search`  
**Parameters:**

| Parameter | Type   | Description                                          |
|-----------|--------|------------------------------------------------------|
| query     | string | Required. The topic to search for research papers.   |
| rows      | int    | Optional. The number of results to return (default: 5). |
| sort      | string | Optional. Sorting method (default: `score`). Can be adjusted for sorting by relevance or date. |

#### **Proofread Text**  
**POST** `/api/proofread`  
**Parameters:**

| Parameter | Type   | Description                                          |
|-----------|--------|------------------------------------------------------|
| text      | string | Required. The text to be proofread and edited for grammar and style. |
| api_key   | string | Required. Your API key to access the proofreading service. |

#### **Rewrite in Academic Style**  
**POST** `/api/academic/rewrite`  
**Parameters:**

| Parameter | Type   | Description                                                                 |
|-----------|--------|-----------------------------------------------------------------------------|
| text      | string | Required. The text to be rewritten in an academic style.                    |
| api_key   | string | Required. Your API key to access the Cohere API and perform the rewrite.     |

#### **Convert Bullet Points to Paragraph**  
**POST** `/api/bullet/convert`  
**Parameters:**

| Parameter | Type   | Description                                           |
|-----------|--------|-------------------------------------------------------|
| text      | string | Required. Bullet points to be converted into a cohesive paragraph. |
| api_key   | string | Required. Your API key to access the conversion service. |

#### **Summarize Text for Presentation Slides**  
**POST** `/api/slides/summarize`  
**Parameters:**

| Parameter | Type   | Description                                                                 |
|-----------|--------|-----------------------------------------------------------------------------|
| text      | string | Required. The text to be summarized into key bullet points for presentation slides. |
| api_key   | string | Required. Your API key for accessing the summarization service.             |

## Documentation

[Documentation](https://linktodocumentation)


## Demo
[Watch the video](https://drive.google.com/uc?export=download&id=1a6Ub5mtKWVFD11Fw6X7IJpdqAc9jzUQo)


