import openai

openai.api_key_path = "./key_openai.txt"
comp = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "Consider the following chat history between friends Ali, Nathan, Kyle, and Robby are computer science majors who love coding and gaming. They met in their freshman year and became fast friends. They often hang out with Jett and Isaac, who are physics/engineering majors and share their passion for science and technology. Jett is dating Kate, a sweet and caring Korean girl who goes to a different school but visits him often. Kate is also close friends with Caterina, a Lebanese music major who has a beautiful voice and plays several instruments. Caterina is dating Jett's brother, who lives in New York, so she spends a lot of time with Jett, Kate and their friends when he's away. The boys consider Kate and Caterina as part of their group and enjoy their company more than each other. Nathan is very talkative and likes to crack jokes. He is proud of his Mexican heritage and often cleans when he is stressed. Ali is Iranian and a smart bozo who likes to tease everyone with inconsiderate remarks such as \"L bozo\". Kyle is Japanese and very smart but sometimes insensitive to others' feelings. He still cares about his friends though and apologizes when he realizes he's hurt them. Robby (drummer) and Jake (minnesotan business major) are white bozos with poor sleep schedules who often stay up late playing video games or watching movies:\n\n\n\nRobby: me when jetts parents\nAli: Luffy be like: \nKate: My dad been mad at me all day and he said it’s because he had a dream where I came home from school with a nose job\nRobby: My friends been mad at me all day and they said it’s because they had a dream where I came home from school with lip filler\nNathan: Based dad\nKate: Well i had a dream where my dad drove our van off a cliff\nRobby: I got some converse\nKate: u missing out\nAli\": I went to the zaza realm and back maybe 3 times that car ride\nRobby: But it's actually spelled seven\nNathan: Yes sir\nCaterina: I was actually in another realm while I was asleep\nJett: Does the realm start with a z\nAli: I threw up at the red highlight\nKate: be prepared to eat ur fill\nKate: r u still gonna be in Cali?\nKate: 😭😭😭😭\nAli: Made my calorie tracking easier tho I didn’t have to track anything I ate last night\nCaterina: Who knows but I just dreamt a full-on action movie and woke like I didn't even sleep 8 hours\nJake: I think I leave a few days before 😔 \nKate: 😭😭😭\nKate: NOOOOOOO\nKate: 💀💀💀💀\nJett: Kid named exhausting\nKate: Kid named spitting rizz\nJett: Denny's\nNathan: LETS GOOOO\nAli: Come to Dennys if ur not a bozo\nNathan: Gym + cardio\nNathan: No can do\nAli: U should’ve j thrown up to not have to worry about it\nKate: BIG SLAYYYY\n\n\n"},
        {"role": "user", "content": "Jake: Kyle almost just got us kicked out of Walmart"},
        {"role": "assistant", "content": "Robby: fucking how"},
        {"role": "user", "content": "I Mike the ball to this mf and he punts it as hard as he could And we got yelled at"}
    ],
)

print(comp.choices[0].message["content"])