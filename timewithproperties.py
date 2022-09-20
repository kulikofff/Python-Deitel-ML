class Time:
    """Класс Time со свойствами, доступными для чтения/записи."""

    def __init__(self, hour=0, minute=0, second=0):
        """Инициализация каждого атрибута."""
        self.hour = hour # 0-23
        self.minute = minute # 0-59
        self.second = second # 0-59

    @property
    def hour(self):
        """Возвращает значение часов."""
        return self._hour
    
    @hour.setter
    def hour(self, hour):
        """Присваивает значение часов."""
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')

        self._hour = hour

    @property
    def minute(self):
        """Return the minute."""
        return self._minute

    @minute.setter
    def minute(self, minute):
        """Set the minute."""
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')

        self._minute = minute

    @property
    def second(self):
        """Return the second."""
        return self._second

    @second.setter
    def second(self, second):
        """Set the second."""
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')

        self._second = second

    def set_time(self, hour=0, minute=0, second=0):
        """Присваивает значения часов, минут и секунд."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        """Возвращает строку Time для repr()."""
        return (f'Time(hour={self.hour}, minute={self.minute}, ' +
        f'second={self.second})')    

    def __str__(self):
        """Выводит объект Time в 12-часовом формате времени."""
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) +
        f':{self.minute:0>2}:{self.second:0>2}' +
        (' AM' if self.hour < 12 else ' PM'))