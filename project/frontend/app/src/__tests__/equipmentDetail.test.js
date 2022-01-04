import { QueryClient, QueryClientProvider } from 'react-query';
import { configure, render as rtlRender, screen } from '@testing-library/react';
import EquipmentDetailScreen from '../screens/EquipmentDetailScreen';

const equipment_mock = {
    object: {
        id: 1,
        post_name: 'Tennis Racket',
        sport_category: 'Tennis',
        link: 'https://www.adidas.com.tr/tr',
        active: true,
        pathToEquipmentPostImage: 'https://gulfgoal.com/en/wp-content/uploads/2021/12/urn-newsml-dpa-com-20090101-211118-99-48608_large_4_3-780x470.jpg',
        description: 'I am selling my tennis racket',
        owner: {
            name: 'Umut',
            surname: 'Gün'
        }
    }
};

function render(children) {
  const queryClient = new QueryClient();
  return rtlRender(<QueryClientProvider client={queryClient}>{children}</QueryClientProvider>);
}

test('equipment', async () => {
  configure({ defaultHidden: true });

  render(<EquipmentDetailScreen data={equipment_mock.object} eq_id={equipment_mock.id} />);

});
