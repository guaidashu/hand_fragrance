"""
author songjie
"""
from app.libs.enums import PendingStatus
from flask_login import current_user


class DriftViewModel:
    @classmethod
    def pending(cls, drifts):
        """
        处理数据
        :param drifts:
        :return:
        """
        returned = []
        for drift in drifts:
            if drift.requester_id == current_user.id:
                you_are = 'requester'
            else:
                you_are = 'gifter'
            pending_status = PendingStatus.pending_str(drift.pending, you_are)
            pending_result = PendingStatus.pending_status(drift.pending)
            r = {
                'drift_id': drift.id,
                'you_are': you_are,
                # 'book_title': drift.gift.book.title,
                # 'book_author': drift.gift.book.author_str,
                'book_title': drift.book_title,
                'book_author': drift.book_author,
                'book_img': drift.book_img,
                'operator': drift.requester_nickname if you_are != 'requester' \
                    else drift.gifter_nickname,
                'date': drift.create_datetime.strftime('%Y-%m-%d'),
                'message': drift.message,
                'address': drift.address,
                'recipient_name': drift.recipient_name,
                'mobile': drift.mobile,
                'status_str': pending_status,
                'status': pending_result
            }
            returned.append(r)
        return returned
