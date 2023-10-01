For the LLM annotation task I used https://claude.ai/chat/.

# Step 1. 

* I asked Claude:

Generate 90 sentences in a single list similar to the following:

- The athlete won a gold medal at the Olympics.

- The legislation was passed after a long debate in the Senate.

* With this prompt Claude listed similar sentences but it only gave 64 sentences, so I had to ask:

You only listed 64 sentences. Can you list 26 more sentences?

# Step 2. 

* I copy pasted the 90 generated sentences in the csv file `llm_generated_posts.csv`.

# Step 3. 

* The Claude chat supports file upload. I uploaded the file I created in step 2 and I asked Claude:

Please annotate the sentences in this csv file as in the following examples and write your answer formatted as the contents of a csv file:

post,topic

The athlete won a gold medal at the Olympics., sports

The legislation was passed after a long debate in the Senate., politics

The discovery of the Higgs boson at CERN marked a milestone in particle physics., science

The swimmer broke the world record in the 100-meter freestyle., sports

The bill received bipartisan support and was signed into law by the president., politics The recent findings on black holes have revolutionized our understanding of space-time., science

The spacecraft successfully docked with the International Space Station., science

The gymnast captured the audience's hearts and took home the bronze medal., sports After months of negotiations, the climate accord was finally agreed upon by the majority of nations., politics

Scientists successfully cloned a sheep, sparking ethical debates worldwide., science

# Step 4. 

* I saved the output generated in step 3 in `llm_labeled_dataset.csv`. 

* The `posts_data.csv` constains the 10 labeled example posts given in the project requiremnts together with the 90 LLM generated and annotated posts/sentences.
