# vLLM

Deployment preset. AMD64/ARM64 registry manifests checked; runtime acceptance pending

GPU model serving through an authenticated OpenAI-compatible endpoint.

## Requirements

- Compatible NVIDIA GPU, CUDA 13 driver and device plugin
- ARM64 image requires NVIDIA SBSA hardware; ordinary ARM CPU nodes are unsupported
- Review model license and access terms
- Persistent model cache; image download is about 10 GB
- GPU execution has not been verified on the local development host

## Credentials

- `inference-api-key`: Clients must supply this key when calling the inference API. Keep this stable and include it in protected backups.
- `model-token`: Hugging Face read token with access to the selected private or gated model. Accept the model's terms upstream first.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://docs.vllm.ai/en/stable/deployment/docker/
- https://docs.vllm.ai/en/stable/configuration/env_vars/

Application license: Apache-2.0 engine; model license varies.
