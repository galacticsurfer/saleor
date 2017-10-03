import React, { PropTypes } from 'react';
import Relay from 'react-relay';

import SaleImg from '../../../images/sale_bg.svg';

const ProductPrice = ({ availability, price }) => {
  const { discount, priceRange } = availability;
  var fullValue = 0;
  var discountPercentage = 0;
  if(discount) {
    fullValue = priceRange.minPrice.gross + discount.gross;
    discountPercentage = (discount.gross / fullValue) * 100;
  }
  else {
    fullValue = priceRange.minPrice.gross;
  }
  const isPriceRange = priceRange && priceRange.minPrice.gross !== priceRange.maxPrice.gross;
  return (
    <div>
      <span itemProp="price">
        <font style={{fontWeight: 'bold', color: 'black'}}><span class="currency">₹</span>{priceRange.minPrice.gross}</font> &nbsp;
        { discount && (<strike><font style={{ fontSize:'0.80rem'}}><span class="currency">₹</span>{fullValue}</font></strike>)} &nbsp;
        { discount && (<font style={{fontSize: '0.70rem', fontWeight: 'bold', color: 'green'}}>{discountPercentage} % off</font>)}
      </span>
    </div>
  );
};

ProductPrice.propTypes = {
  availability: PropTypes.object.isRequired,
  price: PropTypes.object.isRequired
};

export default Relay.createContainer(ProductPrice, {
  fragments: {
    availability: () => Relay.QL`
      fragment on ProductAvailabilityType {
        available,
        discount { gross },
        priceRange {
          maxPrice { gross, grossLocalized, currency },
          minPrice { gross, grossLocalized, currency }
        }
      }
    `
  }
});
