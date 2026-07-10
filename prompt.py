from langchain_core.prompts import PromptTemplate

blog_prompt = PromptTemplate(
    input_variables=["topic","tone","length","audience"],
    template="""
   You are an expert content writer.

   write a {length} blog post.

   Topic:{topic}
   Tone:{tone}
   Audience:{audience}

   Include:
   - Catch Title
   - Introduction
   - 4.5 headings
   - Practical examples
   - Conclusion
   - Key takeways

   Return the responses in Markdown.
"""    
)                                                                                 