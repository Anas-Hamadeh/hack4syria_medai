#!/usr/bin/env python
import warnings
from dotenv import load_dotenv


from hack4syria_medai.crew import Hack4SyriaMedai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run(input: dict = None):
    """
    Run the crew.
    """
    try:
        Hack4SyriaMedai().crew().kickoff(inputs=input)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    load_dotenv(override=True)
    # Process a medical case
    input = {
        "topic": "دكتور، أنا أشعر بخفقان سريع ومفاجئ في القلب، وكأنه ينبض بسرعة كبيرة جدًا بدون سبب واضح. يحدث هذا بشكل متكرر منذ بضعة أشهر، وأحيانًا يستمر لعدة دقائق، وأحيانًا لأكثر من ساعة. عندما يحدث، أشعر بدوخة خفيفة، وأحيانًا ضيق في التنفس، لكنه لا يصل إلى درجة الإغماء. بدأت منذ حوالي 6 أشهر. ألاحظ أنها تحدث غالبًا عندما أكون متوترًا أو بعد شرب القهوة أو ممارسة التمارين الرياضية، لكنها أحيانًا تأتي فجأة حتى عندما أكون مرتاحًا. ثم يعود للوضع الطبيعي بشكل مفاجئ. ليس لدي أي تاريخ سابق لأمراض القلب، ولم أعاني من ارتفاع ضغط الدم أو السكري. لا أتناول أي أدوية يوميًا، ولكن أحيانًا أتناول مسكنات للصداع مثل الباراسيتامول. لا أدخن، ولكن أشرب القهوة يوميًا، حوالي كوبين أو ثلاثة. لا أشرب الكحول. لا أشعر بألم في الصدر، لكن في بعض المرات عندما يكون الخفقان شديدًا، أشعر بضيق خفيف في التنفس وتعرق بسيط. لم أفقد الوعي أبدًا. أحيانًا عندما أحبس نفسي وأحاول أخذ نفس عميق، يخف الخفقان قليلاً. قرأت عن مناورة فالسالفا وجربتها، وأحيانًا تساعد في إيقاف النوبة."
    }  # "Patient complains of chest pain"
    run(input=input)
