import os

from assemblyai_haystack.transcriber import AssemblyAITranscriber
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack import Pipeline
from haystack.components.writers import DocumentWriter

from collect_audio_data import collect_episode_urls


ASSEMBLYAI_API_KEY = os.environ.get("ASSEMBLYAI_API_KEY")
document_store = InMemoryDocumentStore()

indexing = Pipeline()
indexing.add_component("transcriber", AssemblyAITranscriber(api_key=ASSEMBLYAI_API_KEY))
indexing.add_component("writer", DocumentWriter(document_store))
indexing.connect("transcriber.transcription", "writer.documents")

rss_feed = "https://podcasts.files.bbci.co.uk/p02nq0gn.rss"
episode_audio_urls = collect_episode_urls(rss_feed)

for episode in episode_audio_urls:

    indexing.run(
        {
            "transcriber": {
                "file_path": episode,
                "summarization":None,
                "speaker_labels":None
            }
        }
    )

    print("Indexed Document Count:", document_store.count_documents())
    break