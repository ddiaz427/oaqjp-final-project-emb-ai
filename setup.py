from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'emotion_detection = EmotionDetection.emotion_detection:emotion_detector',
        ],
    },
)