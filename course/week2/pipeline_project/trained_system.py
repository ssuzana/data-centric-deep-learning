from src.system import DigitClassifierSystem

system = DigitClassifierSystem.load_from_checkpoint(
    './artifacts/ckpts/train_flow/epoch=2-step=4500.ckpt')

print(system)