logs="""[INFO] Changes detected - recompiling the module! :source
[INFO] Compiling 332 source files with javac [debug release 17] to target/classes
[WARNING] /src/main/java/com/neurio/site/dto/v3/KpiResultV3.java:[21,17] @Builder will ignore the initializing expression entirely. If you want the initializing expression to serve as default, add @Builder.Default. If it is not supposed to be settable during building, make the field final.
[WARNING] /src/main/java/com/neurio/site/dto/v3/KpiResultV3.java:[22,17] @Builder will ignore the initializing expression entirely. If you want the initializing expression to serve as default, add @Builder.Default. If it is not supposed to be settable during building, make the field final.
[WARNING] /src/main/java/com/neurio/site/dto/v3/KpiResultV3.java:[23,17] @Builder will ignore the initializing expression entirely. If you want the initializing expression to serve as default, add @Builder.Default. If it is not supposed to be settable during building, make the field final.
[WARNING] /src/main/java/com/neurio/site/entity/FleetSiteMapWithSiteName.java:[17,1] Generating equals/hashCode implementation but without a call to superclass, even though this class does not extend java.lang.Object. If this is intentional, add '@EqualsAndHashCode(callSuper=false)' to your type.
[WARNING] /src/main/java/com/neurio/site/entity/Address.java:[18,1] Generating equals/hashCode implementation but without a call to superclass, even though this class does not extend java.lang.Object. If this is intentional, add '@EqualsAndHashCode(callSuper=false)' to your type.
[WARNING] /src/main/java/com/neurio/site/entity/Audit.java:[16,1] Generating equals/hashCode implementation but without a call to superclass, even though this class does not extend java.lang.Object. If this is intentional, add '@EqualsAndHashCode(callSuper=false)' to your type.
[WARNING] /src/main/java/com/neurio/site/entity/Site.java:[32,1] Generating equals/hashCode implementation but without a call to superclass, even though this class does not extend java.lang.Object. If this is intentional, add '@EqualsAndHashCode(callSuper=false)' to your type.
[WARNING] /src/main/java/com/neurio/site/dto/registration/RegisterSiteDtoV2.java:[23,1] Generating equals/hashCode implementation but without a call to superclass, even though this class does not extend java.lang.Object. If this is intentional, add '@EqualsAndHashCode(callSuper=false)' to your type.
"""
openai_model="""gpt-4o
"""
from openai import OpenAI;
import json
prompt="List all the warning from this maven log output and explain how to address each one.\n\n```\n"
prompt+=logs
prompt+="\n```"
# print("prompt:", str(prompt))
client = OpenAI()
completion = client.chat.completions.create(
    model=openai_model.strip(),
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(completion.choices[0].message.content)
